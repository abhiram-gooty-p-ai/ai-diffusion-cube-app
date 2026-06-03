import streamlit as st
import streamlit.components.v1 as components
import anthropic
import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv

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

# ─── Chatbot ──────────────────────────────────────────────────────────────────
CHATBOT_SYSTEM = """You are an assistant for the AI Diffusion Cube — a knowledge tool built on real AI deployment experience, organised through the six dimensions framework. You help pathway contributors and the people who engage them.

Your knowledge base is a wiki of pathway pages, synthesis pages, and entity pages drawn from real deployments.

WHO YOU SERVE
- Pathway contributors: people who have deployed AI at scale and are documenting their experience
- Engagement people: those having conversations with contributors to capture pathway knowledge

WHAT YOU CAN DO
Answer questions directly based on what the wiki holds. Infer what the person needs from how they ask — do not ask them to declare a mode.

If someone asks what's missing in a pathway, identify the consequential gaps by dimension and give them as specific re-engagement prompts, not schema labels.
If someone describes a challenge they faced in their deployment, surface what other deployments have documented on the same challenge — with specifics, not generalities.
If someone asks what reusable artifacts they might have, ask concretely by dimension: training materials from E, governance templates from C, data sharing agreements from B, evaluation benchmarks from F, and so on.
If someone asks what a pathway is or how a dimension works, explain it plainly with a real example.
If someone needs to prepare for a contributor conversation, give them targeted questions based on what's known about that deployer's context — not the full template.

HOW TO RESPOND
Be crisp. Answer the question asked. If a gap exists in the wiki, name it honestly rather than pad with generalities. Every factual claim names its deployment source.

If someone lands without a clear question, offer a few prompts to help them orient:
- "I want to check how complete my pathway is"
- "I'm preparing to talk to a contributor — help me know what to ask"
- "What have others done on [challenge]?"
- "What does a good answer to [dimension] look like?"
- "What reusable artifacts might I have from my deployment?"

WHAT YOU DO NOT DO
- You do not invent deployment details not in the wiki
- You do not give general AI deployment advice not grounded in a pathway
- You do not run a structured interview or form-filling session unless the person wants that
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
        st.caption(
            f"Wiki · {pathway_count} pathways · {entity_count} entities · "
            f"{synthesis_count} synthesis · {sector_count} sectors"
        )
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

    # ── Chat history ──────────────────────────────────────────────────────────
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if not st.session_state.chat_history:
        st.markdown(
            "<div style='text-align:center; color:#888; padding: 3rem 0;'>"
            "An assistant for people contributing to and capturing AI deployment pathways — helps check completeness, surface what others have done, identify gaps, and articulate reusable artifacts."
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
            except Exception as e:
                st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
