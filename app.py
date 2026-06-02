import streamlit as st
import streamlit.components.v1 as components
import anthropic
import os
import subprocess
import json
from pathlib import Path
from datetime import date
from dotenv import load_dotenv

load_dotenv()

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "pathways"
WIKI_DIR = BASE_DIR / "wiki"
CLAUDE_MD_PATH = BASE_DIR / "CLAUDE.md"

# ─── Model ────────────────────────────────────────────────────────────────────
MODEL = "claude-opus-4-8"

# ─── Pathway Extraction Engine ────────────────────────────────────────────────
PATHWAY_EXTRACTION_ENGINE = """
## PATHWAY EXTRACTION ENGINE

Before writing any pathway page, execute these nine steps internally:

**Step 1 — Build Evidence Inventory**
Read the entire source document. List every concrete fact: numbers, names, dates, decisions, quotes, costs, timelines, outcomes. Do not interpret yet — just list what is explicitly stated.

**Step 2 — Preserve Operational Detail**
Identify every sentence that describes HOW something was done (not just that it was done). These are the highest-value extracts for a next adopter. Prioritise these above general statements.

**Step 3 — Map Evidence to Dimensions**
For each piece of evidence, assign it to one or more dimensions (A–F) and sub-components. Note which dimensions have thin or no evidence — these become "Not documented." sections.

**Step 4 — Handle Gaps Explicitly**
For every question in the pathway template where evidence is absent, write exactly: Not documented.
Do not infer. Do not fill gaps with generalities from adjacent knowledge. Do not skip questions silently. Every question must appear with either an answer or "Not documented."

**Step 5 — Generate Additional Insights**
After answering all static questions, check: does the source contain any significant insight, decision, or solution not captured by the template questions? If yes, add it under Additional Insights of the relevant dimension. If no, omit the sub-section entirely — do not write "None."

**Step 6 — Distinguish Fact from Interpretation**
Every factual claim must name its deployment. Attribute evidence quality in prose within the sentence. Use formulations like: "field transcripts confirm...", "the deployment team reports...", "this is inferred from cross-deployment patterns...". Do not use emoji markers.

**Step 7 — Preserve Contradictions**
If two pieces of evidence conflict, note both. Do not silently resolve contradictions. Flag unresolved contradictions in the pathway page and in log.md for human review.

**Step 8 — Apply Anti-Fluff Rules**
- No generalised AI advice not grounded in this specific pathway
- No padding thin evidence with adjacent or general knowledge
- No bullet points inside dimension answer sections — prose only
- No H4 or below headings — H1, H2, H3 only
- Summary section: maximum three sentences
- Do not skip questions — every question gets an answer or "Not documented."
- Do not write "None" for empty Additional Insights — omit the sub-section

**Step 9 — Pathway Quality Check**
Before writing any pages, verify:
(a) Every template question is answered or marked "Not documented."
(b) Every factual claim names its deployment
(c) No bullet points inside dimension answer sections
(d) Additional Insights sub-section omitted if nothing to add
(e) log.md will be appended with this ingest entry
(f) index.md will be updated with all new and changed pages
(g) SUMMARY.md will be updated with all new pages in correct section order
"""

# ─── Tool definitions ─────────────────────────────────────────────────────────
INGEST_TOOLS = [
    {
        "name": "read_file",
        "description": "Read a file from the project directory. Use relative paths from the project root.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative path from project root, e.g. 'wiki/pathways/mahavistaar.md'"
                }
            },
            "required": ["path"]
        }
    },
    {
        "name": "write_file",
        "description": "Write content to a file. Creates parent directories if needed. Use for creating or updating wiki pages.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative path from project root, e.g. 'wiki/pathways/new-pathway.md'"
                },
                "content": {
                    "type": "string",
                    "description": "Full content to write to the file"
                }
            },
            "required": ["path", "content"]
        }
    },
    {
        "name": "list_files",
        "description": "List all files in a directory recursively.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative path from project root, e.g. 'wiki/pathways'"
                }
            },
            "required": ["path"]
        }
    },
    {
        "name": "run_command",
        "description": "Run a shell command. Useful for pdftotext and other file processing.",
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "Shell command to execute"
                }
            },
            "required": ["command"]
        }
    }
]

# ─── Tool handlers ─────────────────────────────────────────────────────────────
def handle_tool(tool_name: str, tool_input: dict) -> str:
    if tool_name == "read_file":
        path = BASE_DIR / tool_input["path"]
        try:
            return path.read_text(encoding="utf-8")
        except FileNotFoundError:
            return f"File not found: {tool_input['path']}"
        except Exception as e:
            return f"Error reading file: {e}"

    elif tool_name == "write_file":
        path = BASE_DIR / tool_input["path"]
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(tool_input["content"], encoding="utf-8")
            return f"OK — written: {tool_input['path']}"
        except Exception as e:
            return f"Error writing file: {e}"

    elif tool_name == "list_files":
        path = BASE_DIR / tool_input["path"]
        try:
            if not path.exists():
                return f"Directory not found: {tool_input['path']}"
            files = sorted(f for f in path.rglob("*") if f.is_file())
            return "\n".join(str(f.relative_to(BASE_DIR)) for f in files)
        except Exception as e:
            return f"Error listing files: {e}"

    elif tool_name == "run_command":
        cmd = tool_input["command"]
        try:
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=120
            )
            output = result.stdout
            if result.returncode != 0:
                output += f"\nSTDERR: {result.stderr}"
            return output or "(no output)"
        except subprocess.TimeoutExpired:
            return "Command timed out after 120 seconds"
        except Exception as e:
            return f"Error running command: {e}"

    return f"Unknown tool: {tool_name}"

# ─── Load context helpers ──────────────────────────────────────────────────────
@st.cache_data(ttl=30)
def load_claude_md() -> str:
    return CLAUDE_MD_PATH.read_text(encoding="utf-8")

def load_wiki_context() -> str:
    parts = []
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        rel = md_file.relative_to(BASE_DIR)
        content = md_file.read_text(encoding="utf-8")
        parts.append(f"### File: {rel}\n\n{content}")
    return "\n\n---\n\n".join(parts)

def load_benchmark() -> str:
    path = WIKI_DIR / "pathways" / "mahavistaar.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""

# ─── Ingestion agentic loop ───────────────────────────────────────────────────
def run_ingestion(
    client: anthropic.Anthropic,
    doc_text: str,
    doc_filename: str,
    metadata: dict,
    log_placeholder,
):
    claude_md = load_claude_md()
    benchmark = load_benchmark()
    system_prompt = claude_md + "\n\n" + PATHWAY_EXTRACTION_ENGINE

    benchmark_block = ""
    if benchmark:
        benchmark_block = f"""
The following is the existing mahavistaar.md pathway page. Use it ONLY as a style and quality benchmark — formatting, question structure, prose density, gap handling. Do NOT copy its facts, metrics, wording, numbers, or conclusions. Extract facts exclusively from the source document.

<benchmark>
{benchmark}
</benchmark>
"""

    meta_lines = []
    if metadata.get("deployment_name"):
        meta_lines.append(f"- Deployment name: {metadata['deployment_name']}")
    if metadata.get("contributor"):
        meta_lines.append(f"- Contributor: {metadata['contributor']}")
    if metadata.get("date"):
        meta_lines.append(f"- Contribution date: {metadata['date']}")
    if metadata.get("source_type"):
        meta_lines.append(f"- Source type: {metadata['source_type']}")

    meta_str = "\n".join(meta_lines) if meta_lines else "No metadata provided — infer from document where possible, mark gaps as Not documented."

    user_message = f"""New source document for ingestion into the AI Diffusion Cube wiki.

Filename: {doc_filename}
Metadata:
{meta_str}

{benchmark_block}

Instructions:
- Use mahavistaar.md above ONLY as a style benchmark, not a content source
- Extract facts exclusively from the source document below
- Execute all nine steps of the PATHWAY EXTRACTION ENGINE before writing any pages
- Follow the full ingest protocol from CLAUDE.md: create/update pathway pages, entity pages, sector pages, and update wiki/index.md, wiki/log.md, and SUMMARY.md

<source_document filename="{doc_filename}">
{doc_text}
</source_document>

Begin with Step 1 (evidence inventory), then proceed through all nine steps, then execute the ingest."""

    messages = [{"role": "user", "content": user_message}]
    log_lines = []

    def log(msg: str):
        log_lines.append(msg)
        log_placeholder.text_area(
            "Ingestion log",
            "\n".join(log_lines),
            height=520,
            key=f"log_{len(log_lines)}"
        )

    log(f"▶ Starting ingestion: {doc_filename}")
    log(f"  Document length: {len(doc_text):,} characters")
    log("")

    for iteration in range(1, 40):
        log(f"── API call {iteration} ──────────────────────────────")

        response = client.messages.create(
            model=MODEL,
            max_tokens=8192,
            system=system_prompt,
            tools=INGEST_TOOLS,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        for block in response.content:
            if hasattr(block, "text") and block.text.strip():
                preview = block.text[:600]
                if len(block.text) > 600:
                    preview += f"... [{len(block.text):,} chars total]"
                log(f"[model] {preview}")

        if response.stop_reason == "end_turn":
            log("")
            log("✓ Ingestion complete.")
            break

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    input_preview = json.dumps(block.input)
                    if len(input_preview) > 120:
                        input_preview = input_preview[:120] + "..."
                    log(f"[tool] {block.name}({input_preview})")

                    result = handle_tool(block.name, block.input)

                    result_preview = str(result)
                    if len(result_preview) > 200:
                        result_preview = result_preview[:200] + f"... [{len(str(result)):,} chars]"
                    log(f"  → {result_preview}")

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result),
                    })

            messages.append({"role": "user", "content": tool_results})
        else:
            log(f"[warn] Unexpected stop reason: {response.stop_reason}")
            break

    return log_lines

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

    # API key — env var (local) or Streamlit secrets (cloud)
    api_key = os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        st.error("ANTHROPIC_API_KEY not set. Add it to .env locally or Streamlit Cloud secrets.")
        st.stop()

    client = anthropic.Anthropic(api_key=api_key)

    st.title("AI Diffusion Cube")
    st.caption("Knowledge base of AI deployment pathways for public-interest sectors")

    tab_ingest, tab_chat = st.tabs(["Ingest Documents", "Wiki Chatbot"])

    # ── Tab 1: Ingestion ──────────────────────────────────────────────────────
    with tab_ingest:
        st.header("Ingest Source Documents")
        st.markdown(
            "Upload source documents (PDFs, transcripts, notes) to build or update pathway pages. "
            "The agent follows the full CLAUDE.md ingest protocol and PATHWAY EXTRACTION ENGINE."
        )

        uploaded_files = st.file_uploader(
            "Drop documents here",
            type=["pdf", "txt", "md"],
            accept_multiple_files=True,
            help="PDFs are converted to text via pdftotext. Transcripts and markdown files are read directly.",
        )

        with st.expander("Metadata — provide to skip clarifying questions", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                deployment_name = st.text_input(
                    "Deployment name",
                    placeholder="e.g. MahaVistaar, Bihar Krishi",
                )
                contributor = st.text_input(
                    "Contributor",
                    placeholder="Person and/or organisation",
                )
            with col2:
                contrib_date = st.date_input("Contribution date", value=date.today())
                source_type = st.selectbox(
                    "Source type",
                    [
                        "deployment pathway",
                        "field report",
                        "framework document",
                        "governance template",
                        "transcript",
                        "other",
                    ],
                )

        ingest_btn = st.button(
            "Start Ingestion",
            type="primary",
            disabled=not uploaded_files,
        )

        if ingest_btn and uploaded_files:
            for uploaded_file in uploaded_files:
                st.divider()
                st.subheader(f"Ingesting: {uploaded_file.name}")

                # Save raw file
                save_path = RAW_DIR / uploaded_file.name
                save_path.write_bytes(uploaded_file.getvalue())

                # Extract text
                with st.spinner("Extracting text..."):
                    if uploaded_file.name.lower().endswith(".pdf"):
                        result = subprocess.run(
                            f'pdftotext "{save_path}" -',
                            shell=True,
                            capture_output=True,
                            text=True,
                        )
                        doc_text = result.stdout
                        if not doc_text.strip():
                            st.error(
                                "pdftotext returned empty output. "
                                "Ensure poppler is installed: brew install poppler"
                            )
                            continue
                    else:
                        doc_text = uploaded_file.getvalue().decode("utf-8", errors="replace")

                st.info(f"Extracted {len(doc_text):,} characters. Running ingestion agent...")

                log_placeholder = st.empty()

                metadata = {
                    "deployment_name": deployment_name,
                    "contributor": contributor,
                    "date": str(contrib_date),
                    "source_type": source_type,
                }

                try:
                    run_ingestion(client, doc_text, uploaded_file.name, metadata, log_placeholder)
                    st.success(f"✓ Ingestion complete: {uploaded_file.name}")
                    st.cache_data.clear()
                except Exception as e:
                    st.error(f"Ingestion error: {e}")

    # ── Tab 2: Chatbot ────────────────────────────────────────────────────────
    with tab_chat:

        # ── Compact top bar ───────────────────────────────────────────────────
        pathway_count  = len(list((WIKI_DIR / "pathways").glob("*.md")))  if (WIKI_DIR / "pathways").exists()  else 0
        entity_count   = len(list((WIKI_DIR / "entities").glob("*.md")))  if (WIKI_DIR / "entities").exists()  else 0
        synthesis_count = len(list((WIKI_DIR / "synthesis").glob("*.md"))) if (WIKI_DIR / "synthesis").exists() else 0
        sector_count   = len(list((WIKI_DIR / "sectors").glob("*.md")))   if (WIKI_DIR / "sectors").exists()   else 0

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

        # ── Chat history ──────────────────────────────────────────────────────
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

        # Scroll to bottom after history renders so latest messages are visible
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

        # ── Input (pinned to bottom by Streamlit) ─────────────────────────────
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
