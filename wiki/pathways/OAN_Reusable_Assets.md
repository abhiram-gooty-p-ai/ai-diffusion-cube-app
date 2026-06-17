# OAN — Reusable Assets
## Solution Patterns, Technical Components, and Governance Artifacts

---

## 1. Solution Patterns

### Architecture

**Problem:** LLM costs become unsustainable as usage scales.

**Solution:** Migrate high-volume flows to self-hosted open-source models; retain managed API as fallback only. Profile cost by use case before migrating — identify the dominant flow and optimise for its worst case.

---

**Problem:** Self-hosted infrastructure and managed APIs create opposing pressures on cost and reliability.

**Solution:** Dual-provider architecture: self-hosted as primary, managed API as automatic fallback triggered only by infrastructure faults — not answer quality. Define a tunable concurrency cap that spills to managed API on overflow rather than queuing users.

---

**Problem:** The system gets locked with a vendor with no exit path.

**Solution:** Build a provider abstraction layer at the start — resolve provider at configuration time, not in application code. Migration between providers becomes transparent to the application.

---

### Population & Access

**Problem:** Target population cannot reach the system through available channels.

**Solution:** Voice-first as an architectural requirement — IVR short codes on basic feature phones, not a smartphone add-on. Support multiple channels — voice, WhatsApp, app, web — converging into the same processing pipeline.

---

**Problem:** The system works in one language but the population speaks many.

**Solution:** Build multilingual ASR and TTS pipeline as core infrastructure, not a post-launch addition. Develop domain-specific bilingual glossary to bridge regional language and institutional terminology — general translation models fail on specialised terms.

---

### Data

**Problem:** Data needed to serve users is fragmented across institutions.

**Solution:** Federated tool architecture — AI connects to each institutional source at query time via API; data does not move into a central repository. Each institution retains ownership and governance of its own data; open network protocols provide the interoperability layer.

---

**Problem:** AI responses have no traceable source — no institution is accountable for what the system says.

**Solution:** Every claim the system makes must be retrieved from a named institutional source at the time of the query — the system does not answer from its own model memory. Surface institutional source attribution visibly to the user on every response.

---

### Institution

**Problem:** The deployment is treated as a technology project — commissioned by the institution but not owned by it — leaving no one with authority over the governance, data sharing, and outcomes that the technology alone cannot deliver.

**Solution:** Nominate a named senior sponsor and nodal officers across relevant departments before build begins. Frame the deployment as an institutional capability.

---

**Problem:** Data sharing agreements between institutions take longer to negotiate than the project expects.

**Solution:** Begin data sharing negotiations before technical build starts — treat agreement timelines as the critical path, not a parallel workstream. Align data sharing across all required institutions as system leadership work before any build begins.

---

### Trust & Adoption

**Problem:** End users distrust AI-generated answers for decisions.

**Solution:** Position AI as delivery layer not authority — every answer cites the institution whose knowledge it draws from. The institution stands behind every answer; AI makes institutional knowledge reachable, it does not replace institutional accountability.

---

**Problem:** The AI system makes claims the institution has not authorised it to make.

**Solution:** Define explicitly what the AI can and cannot do — domain validation, content safety, and policy-sensitive query classification enforced by an independent moderation layer. Every claim flows through a verified tool call to an authoritative source; the AI does not answer from memory.

---

### Ecosystem

**Problem:** The deployment requires capabilities and data that no single institution possesses — but the institutions that collectively possess them were never designed to work together.

**Solution:** Map the full enabler ecosystem before build — identify which layer each actor belongs to, what they contribute, and what governance arrangement allows their contribution to flow. Design participation so each actor's own interest is served — shared mission alone will not sustain coordination across actors with different mandates and incentives.

---

## 2. Reusable Technical Components

| Component | What it is | Reuse condition |
|---|---|---|
| **Agentic AI architecture** | Four-layer decision engine: moderation layer, reasoning layer, tool orchestration, response generation. Each layer decoupled and independently adaptable. | Any conversational AI deployment requiring multi-source data retrieval with verified, source-attributed responses. |
| **Voice pipeline** | ASR + TTS + turn detection pipeline optimised for low-literacy, multilingual users on basic feature phones. Handles regional languages and code-switching. | Any deployment targeting populations without smartphones or text literacy. |
| **Document ingestion pipeline** | OCR, chunking, metadata tagging, and vector indexing pipeline for converting unstructured government documents and publications into a queryable RAG corpus. | Any deployment where the knowledge base consists of scanned or unstructured institutional documents. |
| **Multilingual domain glossary** | Bidirectional terminology bridge between regional language and institutional or technical language. Built per domain and per language pair. | Any deployment serving multilingual populations in specialised domains where general translation models produce errors. |
| **Dual-provider inference stack with prefix caching** | Provider abstraction layer with self-hosted vLLM as primary and managed API as automatic fallback. Concurrency cap tunable without code changes. Prefix caching skips recomputation of repeated conversation prefixes. | Any deployment self-hosting models at scale with multi-turn conversational flows and reliability requirements. |
| **Open network protocol layer** | Beckn-based interoperability layer enabling standardised discovery and interaction across independent institutional data providers without centralising data. | Any deployment connecting multiple institutional data sources under federated governance. |
| **Seven open-source DPGs** | Knowledge Engine, Memory Layer, Trust Layer, Agent Core, Action Gateway, Reach Layer, Learning Layer — unbundled building blocks assemblable into a production-grade voice AI system. Works with any speech models and LLMs. | Any government department or district administration deploying voice AI without building from scratch. |
| **Model evaluation benchmark methodology** | Framework for building domain-specific evaluation sets from real user interactions; methodology for scoring model performance against ground truth in a specialised domain. | Any deployment requiring ongoing assessment of AI output quality where general benchmarks do not capture domain-specific accuracy. |

---

## 3. Governance Artifacts

| Artifact | What it is | Reuse condition |
|---|---|---|
| **Data sharing agreement framework** | Template structure for MOU between institutions governing what data can be accessed, by whom, under what consent conditions, and for what purpose. | Any deployment requiring data access across institutional boundaries. |
| **Consent architecture model** | Framework for capturing, storing, and operationalising user consent at the point of data creation. Aligned with DPDP 2023. Consent is a built-in property of the architecture, not a post-facto audit exercise. | Any deployment in India handling personal data of citizens; adaptable to equivalent frameworks in other jurisdictions. |
| **AI authority boundary model** | Framework defining what the AI can and cannot speak on behalf of — which institutions, which knowledge sources, which scope of decisions. Separates AI as delivery layer from institution as authority. | Any deployment where AI speaks on behalf of public institutions in high-stakes advisory domains. |
| **Institutional ownership model** | Template for nominating sponsor, nodal officers, and cross-departmental steering structure. Defines roles across the deploying department, IT, and field operations before build begins. | Any deployment requiring coordination across more than one government department or institution. |

---

## 4. Gaps — Information Not in the Source Documents

1. At twelve months, what would you expect to observe in a farmer's life — not in the system's logs — that would tell you this worked? And for any of the live deployments, has anything like that been observed yet?
2. Which body has the authority to determine what MahaVistaar can and cannot claim on behalf of the state — and what happens when that boundary is crossed?
3. How was the initial deployment funded — which institution's budget, under what mechanism? And who bears the ongoing cost of the GPU cluster and the operational team — state government budget, central scheme, development partner, or something else?
4. For the core actors — ICAR, IMD, AgriStack, the state agricultural universities — was their data contribution under a formal agreement, an informal arrangement, or a public mandate? And if any of them had withdrawn, what would have broken?
5. Were extension officers or agriculture department staff resistant to the system — and what form did that resistance take?
6. Today, in normal operations, who decides when the model needs retraining, when the advisory corpus needs updating, and when a guardrail needs changing? Is that a named role, a team, or is it still the pilot team?
7. When a farmer receives a wrong or harmful answer — wrong pest treatment advice, wrong scheme eligibility, wrong mandi price — what is the path from that error to a fix? Who finds out, who decides what to do, and how are the guardrails updated so it doesn't happen again?
8. Which specific regulatory or policy constraints — DPDP obligations, government procurement rules, NIC hosting requirements — shaped how the deployments were structured? And were any of them obstacles that required a workaround?
