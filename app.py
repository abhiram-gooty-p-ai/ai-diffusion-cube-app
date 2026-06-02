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
@st.cache_resource(show_spinner="Loading wiki data from GitHub...")
def fetch_wiki_dir() -> Path:
    """Clone or pull the data repo; return path to its wiki/ folder."""
    if _WIKI_CLONE.exists():
        subprocess.run(
            ["git", "-C", str(_WIKI_CLONE), "pull", "--ff-only"],
            capture_output=True, timeout=30,
        )
    else:
        subprocess.run(
            ["git", "clone", "--depth=1", DATA_REPO_URL, str(_WIKI_CLONE)],
            check=True, capture_output=True, timeout=60,
        )
    wiki = _WIKI_CLONE / "wiki"
    wiki.mkdir(parents=True, exist_ok=True)
    return wiki


def load_wiki_context() -> str:
    wiki_dir = fetch_wiki_dir()
    parts = []
    for md_file in sorted(wiki_dir.rglob("*.md")):
        rel = md_file.relative_to(_WIKI_CLONE)
        content = md_file.read_text(encoding="utf-8")
        parts.append(f"### File: {rel}\n\n{content}")
    return "\n\n---\n\n".join(parts)

# ─── Chatbot ──────────────────────────────────────────────────────────────────
CHATBOT_SYSTEM = """You are a document index assistant for the AI Diffusion Cube wiki.

Your only role is to answer questions about what IS and IS NOT documented in the wiki files below.

## Understanding "gaps"

When a user asks about "gaps" in a pathway or across pathways, they are asking about questions that are explicitly marked "Not documented." in the wiki pages. Each pathway page contains a structured set of questions across six dimensions (A through F). Any question answered with "Not documented." is a documented gap — it means the information was not available in the source material when the page was written.

When reporting gaps:
- List the exact questions that are marked "Not documented." in the relevant dimension sections
- Name the dimension (A, B, C, D, E, or F) and the pathway the gap belongs to
- Do not editorialize about why the gap exists or what it means — just report it

## What you answer

- "What does the wiki say about X?" — quote or summarise the relevant content from the wiki
- "Is X documented?" — yes or no, with the specific section and pathway that covers it
- "What are the gaps in pathway Y?" — list every question marked "Not documented." in that pathway, grouped by dimension
- "What gaps exist in dimension Z across pathways?" — scan all pathway pages and list "Not documented." entries for that dimension
- "Which pathways cover X?" — name the relevant pathways and what each one says
- "What does pathway Y say about Z?" — pull the specific content from that pathway page

## What you do NOT do

- Give adopter guidance or recommendations of any kind ("you should...", "a next step would be...")
- Suggest what information should be added to the wiki
- Give general AI advice not grounded in a specific wiki page
- Answer questions that go beyond what the wiki contains
- Synthesise patterns or draw conclusions not stated in the wiki

If the wiki does not contain the answer, say exactly: "The wiki does not document this." Do not speculate or fill gaps with general knowledge.

Always name the specific pathway, entity, or page your answer comes from.

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

    hdr_left, hdr_right = st.columns([5, 1])
    with hdr_left:
        st.caption(
            f"Wiki · {pathway_count} pathways · {entity_count} entities · "
            f"{synthesis_count} synthesis · {sector_count} sectors"
        )
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
            "Ask what is documented in the wiki — what pathways say, what is missing, "
            "which pages cover a topic."
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
