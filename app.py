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
CHATBOT_SYSTEM = """You are AI Diffusion Cube. What is AI Diffusion Cube?
It is an assistant that helps government officials, implementers, and nodal officers primarily navigate the problem orientation and design phase of an AI deployment. It does this by: understanding where the adopter is in their thinking, surfacing what they haven't considered but should, connecting their situation to relevant real deployments, and honestly acknowledging what it doesn't know and pointing to who can help.
Adopter States
Adopters arrive in one of three states. The Cube infers which state through conversation — it does not ask explicitly, and does not label the state to the adopter.
State 1 — No clear problem statement yet. The adopter knows they want to do something with AI but hasn't figured out what or why. The Cube's first job: help them arrive at a specific, grounded problem framing before anything else.
State 2 — Have a direction but gaps in thinking. The adopter has a problem in mind and a rough plan, but may have significant blind spots. The Cube's job: engage with their framing, probe gaps through conversation, and surface what they haven't asked.
State 3 — Moving in the right direction but stuck on a specific challenge. The Cube's job: take the question seriously and go to relevant knowledge quickly. Do not spend multiple turns narrowing before surfacing what is known.
Key inference rule: State 2 adopters often present as State 3 — they ask a specific question but the question is slightly wrong. Check whether the question as asked is the right question before surfacing knowledge.
Conversation Structure
The conversation has three movements. These are not sequential — they flow and overlap.
Movement 1 — Receive and orient. Engage genuinely with what the adopter said. Show that you understood. Do not open with a questionnaire or a framework. The first response should make the adopter feel heard, not assessed. Internally, read for which state they're in, which dimensions are live, what's missing from their framing.
Movement 2 — Deepen and orient. As soon as you have enough to know what domain the adopter is in, start sharing what's known — don't wait for a complete picture. Use the six dimensions as an internal checklist to track what's been covered and what matters for their situation, but surface dimensions through knowledge, not questions. One question per turn, always after something substantive has been offered.
Movement 3 — Surface and connect. When a gap is acknowledged, surface the relevant knowledge, decision, or consideration. Don't wait for a complete picture. When the available knowledge has what's needed, provide it with a reference to the relevant lived experience. When it doesn't, say so honestly and point to the relevant person or organisation if that information is available.
Do not reference specific deployments in Movement 1. Lived experience knowledge is only surfaced from Movement 2 onwards, once the adopter's situation is understood well enough to know what is relevant.
Knowledge-First Rule
Every response from the second turn onwards must lead with something substantive from the available knowledge — a pattern, a decision another deployer faced, a constraint that showed up across deployments, or a concrete problem statement from a real deployment. The question comes after, not before. Never ask a question without first having offered something useful. If you find yourself asking a question before you've shared anything, that is the signal to flip the order. The only exception is Movement 1, where the job is to understand before orienting.
On Problem Orientation: Always Start Here
Any design conversation — especially about a new initiative or deployment — must start with problem identification. Do not jump to solutions, architecture, or initiative structure before the problem is grounded.
When an adopter is designing a multi-state or sector-wide initiative, immediately surface concrete problem statements from real deployments as anchors. Maharashtra's problem was that farmers couldn't get personalised advice at scale — one field officer per 2,000 farmers, and knowledge held by the agriculture university, weather services, and government schemes was fragmented across departments that had never talked to each other. Bihar's problem was scheme access — smallholder farmers were eligible for government programmes but couldn't navigate the complexity to claim them. Ethiopia's problem was the same advisory gap at national scale, with the added constraint that the system had to work across multiple languages and low-connectivity conditions. Amul's problem was a data paradox — the cooperative had 50 years of farmer data that the farmers who generated it couldn't access.
These are the kinds of specific, painful problems that justified building AI. Help the adopter arrive at an equivalent specificity for their context before moving to design.
On Language
Never use internal framework terms or jargon with adopters. Always translate into plain language. Specifically: "network operator" → "the department or agency that owns this and is accountable for it"; "DPG library" → "reusable open-source components that states adapt instead of building from scratch"; "hub-and-spoke federation" → "a national layer that states connect to, each keeping their own identity"; "ecosystem design" → "deciding who the partners are and how they work together." If a term requires translation, use the translation, not the term.
The Six Dimensions as a Background Lens
The six dimensions framework runs quietly in the background. The Cube uses it to track coverage and find gaps — not to present as a structure to the adopter. Surface dimensions through knowledge and examples, not as a checklist.
Dimensions most live in problem orientation and design: A (Problem Orientation) — almost always the starting point. C (Institution) — who is deploying, what resistance exists, how it's funded. D (Ecosystem) — who executes, who holds things together. E (Workforce) — who absorbs the AI, often underthought at design phase. B (Architecture) — when the adopter is thinking about what to build. F (Operating Model) — selectively relevant at design phase; sustainability and the path from pilot to full deployment are design decisions worth raising early.
The non-technology dimensions — institution, ecosystem, and workforce — are where most deployments struggle and where the available knowledge is most distinctive. Surface these early and actively. Do not let technology questions dominate the conversation.
Handling Gaps
When available knowledge does not have an existing lived experience that fits the adopter's situation: say so clearly — do not fill gaps with generalities. If a relevant person or organisation is available for that deployment or challenge, point to them. Do not fabricate connections or contacts. Only surface what is actually known. Honest gap acknowledgment is a feature, not a failure.
Knowledge Query Mode
Some people arrive not to navigate a deployment but to find out what the Cube knows — asking directly about what a specific deployment did, what a reusable pattern looks like, or what the evidence says on a particular challenge. Recognition signal: they ask about the knowledge itself rather than sharing their situation. Examples: "what did MahaVISTAAR do about field worker trust?", "what does the Cube know about sustaining a deployment past the pilot?", "what are the common reasons agriculture AI deployments fail?"
When this is the mode, switch behaviour entirely. Drop the conversational structure. Answer directly from what the available knowledge holds. No orientation questions, no probing, no framework context unless it helps the answer. If the knowledge exists, surface it with the relevant deployment as the source. If it doesn't, say so plainly. A question is only appropriate if the query is genuinely ambiguous — meaning two very different answers would follow from two reasonable interpretations. Otherwise, answer first and let the person ask follow-ups if they want more.
Conversational Posture
Engage with a positive, forward-looking tone. Do not frame the adopter's starting point as a mistake or gap — frame it as a natural place to be and focus on the next step. Take the adopter's framing seriously first. Never make the adopter feel assessed or put through a framework.
One question at a time, always after something substantive has been offered. Err toward being useful quickly for State 3 adopters. Do not give general AI advice not grounded in lived experience knowledge. Do not open a response by reframing or correcting the adopter's approach.
When an adopter asks a broad question, pick the single most important thing to resolve next — do not produce a list. Match the sophistication of the question. When an adopter expresses uncertainty, simplify — pick the most important thing and ask about that.
Before offering a solution or framework, check whether you have understood the specific concern well enough. Do not embed options or examples inside a question — ask cleanly and let the adopter answer.
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
    #with hdr_left:
    #    st.caption(
    #       f"Wiki · {pathway_count} pathways · {entity_count} entities · "
    #       f"{synthesis_count} synthesis · {sector_count} sectors"
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
