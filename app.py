import streamlit as st
import streamlit.components.v1 as components
import anthropic
import os
import subprocess
import base64
import threading
import time
import uuid
from pathlib import Path
from dotenv import load_dotenv
import requests

load_dotenv()

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent

DATA_REPO_URL = "https://github.com/kameshbhr/ai-diffusion-cube-wiki.git"
_WIKI_CLONE = Path("/tmp/ai-cube-wiki")

# ─── Model ────────────────────────────────────────────────────────────────────
MODEL = "claude-opus-4-8"

# ─── Wiki data ────────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner="Cloning wiki from GitHub...")
def fetch_wiki_dir() -> Path:
    """Clone the data repo once; return path to its wiki/ folder."""
    if not _WIKI_CLONE.exists():
        subprocess.run(
            ["git", "clone", "--depth=1", DATA_REPO_URL, str(_WIKI_CLONE)],
            check=True, capture_output=True, timeout=60,
        )
    wiki = _WIKI_CLONE / "wiki"
    wiki.mkdir(parents=True, exist_ok=True)
    return wiki


@st.cache_data(ttl=300, show_spinner="Syncing wiki from GitHub...")
def load_wiki_context() -> str:
    """Pull latest commits and re-read all wiki files every 5 minutes."""
    subprocess.run(
        ["git", "-C", str(_WIKI_CLONE), "pull", "--ff-only"],
        capture_output=True, timeout=30,
    )
    wiki_dir = fetch_wiki_dir()
    parts = []
    for md_file in sorted(wiki_dir.rglob("*.md")):
        rel = md_file.relative_to(_WIKI_CLONE)
        content = md_file.read_text(encoding="utf-8")
        parts.append(f"### File: {rel}\n\n{content}")
    return "\n\n---\n\n".join(parts)

# ─── Conversation logging ─────────────────────────────────────────────────────
def _push_log(session_id: str, history: list[dict], token: str, repo: str) -> None:
    date = time.strftime("%Y-%m-%d")
    filename = f"logs/{date}_{session_id[:8]}.md"
    url = f"https://api.github.com/repos/{repo}/contents/{filename}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    lines = [f"# Conversation Log\n\n**Session:** `{session_id}`  \n**Date:** {date}\n\n---\n\n"]
    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        lines.append(f"### {role}\n\n{msg['content']}\n\n---\n\n")
    encoded = base64.b64encode("".join(lines).encode("utf-8")).decode()

    sha = None
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            sha = r.json().get("sha")
    except Exception:
        pass

    payload = {"message": f"log: session {session_id[:8]}", "content": encoded}
    if sha:
        payload["sha"] = sha
    try:
        requests.put(url, json=payload, headers=headers, timeout=15)
    except Exception:
        pass


def save_conversation(session_id: str, history: list[dict]) -> None:
    token = st.secrets.get("GITHUB_TOKEN", "") or os.environ.get("GITHUB_TOKEN", "")
    repo = st.secrets.get("LOGS_REPO", "") or os.environ.get("LOGS_REPO", "")
    if not token or not repo:
        return
    threading.Thread(
        target=_push_log,
        args=(session_id, history, token, repo),
        daemon=True,
    ).start()


# ─── Chatbot ──────────────────────────────────────────────────────────────────
CHATBOT_SYSTEM = """You are AI Diffusion Cube — a knowledge tool built on real AI deployment experiences, organised through the six dimensions framework.

WHAT YOU CAN DO
Answer questions directly based on what the wiki holds. Infer what the person needs from how they ask.

HOW TO RESPOND
Answer the question asked in a simple language. Be crisp. If a gap exists in the wiki, name it honestly rather than pad with generalities. Every factual claim names its deployment source.
If someone lands without a clear question, offer a few prompts to help them orient.

WHAT YOU DO NOT DO
- You do not invent deployment details not in the wiki
- You do not give general AI deployment advice not grounded in a pathway
- When direct human connection is more valuable than what the wiki holds, say so.
The current wiki content is provided below."""


def run_chat_stream(client: anthropic.Anthropic, user_message: str, history: list[dict]):
    wiki_context = load_wiki_context()
    system = CHATBOT_SYSTEM + f"\n\n## Current Wiki Content\n\n{wiki_context}"

    api_messages = [{"role": m["role"], "content": m["content"]} for m in history]
    api_messages.append({"role": "user", "content": user_message})

    with client.messages.stream(
        model=MODEL,
        max_tokens=4096,
        system=system,
        messages=api_messages,
    ) as stream:
        for text in stream.text_stream:
            yield text

# ─── Streamlit UI ─────────────────────────────────────────────────────────────
def main():
    st.set_page_config(
        page_title="AI Diffusion Cube",
        page_icon="🧊",
        layout="wide",
    )

    api_key = os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        st.error("ANTHROPIC_API_KEY not set. Add it to .env locally or Streamlit Cloud secrets.")
        st.stop()

    client = anthropic.Anthropic(api_key=api_key)

    st.title("AI Diffusion Cube")

    # ── Compact top bar ───────────────────────────────────────────────────────
    _wd = fetch_wiki_dir()
    pathway_count   = len(list((_wd / "pathways").glob("*.md")))  if (_wd / "pathways").exists()  else 0
    entity_count    = len(list((_wd / "entities").glob("*.md")))  if (_wd / "entities").exists()  else 0
    synthesis_count = len(list((_wd / "synthesis").glob("*.md"))) if (_wd / "synthesis").exists() else 0
    sector_count    = len(list((_wd / "sectors").glob("*.md")))   if (_wd / "sectors").exists()   else 0

    hdr_left, hdr_mid, hdr_right = st.columns([5, 1, 1])
    with hdr_left:
    #    st.caption(
    #        f"Wiki · {pathway_count} pathways · {entity_count} entities · "
    #        f"{synthesis_count} synthesis · {sector_count} sectors"
    #    )
    with hdr_mid:
        if st.button("Refresh Wiki", use_container_width=True):
            load_wiki_context.clear()
            st.rerun()
    with hdr_right:
        if st.session_state.get("chat_history"):
            if st.button("Clear", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()

    st.divider()

    # ── Session ID for logging ────────────────────────────────────────────────
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())

    # ── Chat history ──────────────────────────────────────────────────────────
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if not st.session_state.chat_history:
        st.markdown(
            "<div style='text-align:center; color:#888; padding: 3rem 0;'>"
            "An assistant that makes lived experience from real AI deployments accessible and reusable for the next person attempting something similar."
            "</div>",
            unsafe_allow_html=True,
        )

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Auto-scroll to bottom after history renders
    if st.session_state.chat_history:
        components.html(
            """<script>
            setTimeout(() => {
                const main = window.parent.document.querySelector('section[data-testid="stMain"]');
                if (main) main.scrollTop = main.scrollHeight;
            }, 100);
            </script>""",
            height=0,
        )

    # ── Input (pinned to bottom by Streamlit) ─────────────────────────────────
    if prompt := st.chat_input("Ask what's in the wiki..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                answer = st.write_stream(
                    run_chat_stream(client, prompt, st.session_state.chat_history[:-1])
                )
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": answer}
                )
                save_conversation(
                    st.session_state.session_id,
                    st.session_state.chat_history,
                )
            except Exception as e:
                st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
