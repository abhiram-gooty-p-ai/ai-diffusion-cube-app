# Voice AI + Project Astitva — Reusable Assets
## Solution Patterns, Technical Components, and Governance Artifacts

---

## 1. Solution Patterns

### Population & Access

**Problem:** A significant portion of the target population speaks languages for which no usable AI models exist — they are excluded not by lack of devices but by absence of their language in the digital ecosystem.

**Solution:** Treat language data creation as a prerequisite deployment activity, not a downstream technical task. Build the dataset before building the application. Once a language enters the digital ecosystem, all future AI services built on that infrastructure become accessible to its speakers.

---

### Data

**Problem:** No training data exists for a low-resource language — there are native speakers but no written corpus, no recordings, no transcriptions.

**Solution:** Community-participatory data collection: recruit native speakers as contributors, elders as language anchors, youth as validators and digitisers. Compensate fairly and transparently. A three-tier quality structure (contributors → checkers → validators/subject experts) with parallel production and validation tracks maintains quality at speed.

---

**Problem:** Voice data collected on high-quality devices (16kHz smartphones, studio) does not match the low-quality audio signal (8kHz telephony lines) the model will actually face in deployment.

**Solution:** Collect a portion of training data on the same channel quality — telephony-grade 8kHz — that the deployed system will use. Lab-quality data alone produces a model that degrades in real-world conditions.

---

**Problem:** Collected speech data is all read-aloud from written sentences — but conversational speech has different cadence, vocabulary, and pattern from read speech.

**Solution:** Include spontaneous and conversational speech recordings as a distinct data collection category, not just read-aloud sentences. The model will face conversation, not dictation.

---

### Trust & Adoption

**Problem:** Communities are suspicious of data collection — fear around surveillance, misuse, and loss of control over their own language.

**Solution:** Build trust before building technology. Run repeated field visits, open Q&A sessions, and public events that explain purpose, data use, and community ownership. Frame participation as contribution (Tribaldaan — language donation) not extraction. Compensation must be fair, transparent, and tied to verified contributions.

---

### Architecture

**Problem:** Voice AI deployed for one direction (inbound citizen calls) cannot handle the outbound use case that emerges later — the architecture was not designed for it.

**Solution:** Design the voice architecture for both inbound and outbound from the start. Outbound (institution calling citizen) and inbound (citizen calling institution) have different technology requirements. Locking into a one-way architecture forecloses the outbound use case, which typically emerges once inbound proves value.

---

**Problem:** Deploying voice AI on a single vendor creates lock-in — if the vendor fails or underperforms, the deployment is stuck.

**Solution:** Run multiple vendors in parallel from pilot stage. Split traffic across two or three vendors (e.g. 33/33/33 or 60/20/20). This enables real-world comparative evaluation, maintains healthy cost competition, and provides fallback. Hard learning: single-vendor dependency is expensive to exit.

---

**Problem:** Backend data retrieval takes several seconds — on a telephone line this appears as dead silence and users hang up.

**Solution:** Build hold messages into the voice pipeline: any backend response delay beyond a threshold triggers an audio acknowledgement ("please hold on a moment") to maintain the perception of a live conversation. This is a required peripheral configuration, not an optional enhancement.

---

**Problem:** End-to-end voice models (speech-to-speech) offer low latency and naturalness but are not configurable for domain-specific constraints.

**Solution:** Use a component architecture (ASR + LLM + TTS) rather than end-to-end speech-to-speech models for any deployment requiring domain customisation, safety guardrails, or cost control. End-to-end models are not yet configurable, controllable, or cost-viable for institutional deployments.

---

**Problem:** A voice system designed only for high-connectivity telephony cannot serve populations in low-connectivity environments.

**Solution:** For low-connectivity or offline deployment contexts, evaluate edge-based architectures: quantised small language models embedded in low-grade smartphones that operate without internet. The infrastructure assumption must match the deployment environment.

---

### Institution

**Problem:** A low-resource language effort requires many actors (speakers, annotators, linguists, model builders, hosting providers, application deployers) who have no mechanism to find each other.

**Solution:** Designate a neutral orchestrator who maps the full actor ecosystem and connects them. IIT Madras did not know the Nandurbar effort was happening — there was no connection mechanism. A neutral orchestrator fills this gap and prevents duplication of effort across actors who are solving the same problem in isolation.

---

**Problem:** District-level deployment has no long-term institutional home — when the district effort ends, the work is not sustained.

**Solution:** Design the handoff to a higher institutional tier from the start. In Astitva: district work transitioned to state (MahaVISTAAR integration + tribal department ownership) and national (Bhashini repository). Each tier has a defined role: district builds, state sustains, national makes accessible.

---

### Ecosystem

**Problem:** Voice AI ecosystem has many providers but adopters cannot evaluate which to select — too many choices, unclear criteria.

**Solution:** Before selecting providers, define the use case requirements precisely: which languages, which channels (inbound/outbound/WhatsApp), what conversation length, what latency tolerance. Selection criteria follow from use case requirements. Without this clarity, provider selection is arbitrary.

---

### Sustainability

**Problem:** The deployed model and dataset are owned by the implementing vendor — the institution has no ongoing access, control, or ability to update.

**Solution:** Publish datasets to open national infrastructure (Bhashini). Use open-source model hosting where possible. Community ownership of the dataset is a sustainability mechanism — it does not depend on any single vendor remaining engaged.

---

### Problem Framing

**Problem:** A voice AI system is built and tested by the technical team alone — when it reaches citizens it fails on language, safety, and institutional appropriateness in ways that lab testing did not surface.

**Solution:** In-house human testing by the deploying institution is non-negotiable before public launch. A multi-stage process: technical team first, then a limited set of locally-deployed government testers, then a larger state-level group with structured feedback capture. Each stage gates the next. The institution's reputation is at stake — outsourcing testing entirely to a third party removes the institutional lens that catches what automated tests miss.

---

## 2. Reusable Technical Components

| Component | What it is | Reuse condition |
|---|---|---|
| **Community voice data collection platform** | Mobile app-based platform for recording, transcription, and validation of speech data. Supports three parallel task tracks (contribution, checking, validation) tracked by digital dashboards and leaderboards. Karya's platform used in Astitva. | Any deployment requiring creation of a speech dataset for a low-resource language where no prior corpus exists. |
| **Three-tier community data quality structure** | Operational model: contributors and field participants at base, checkers and reviewers in middle tier, validators and subject experts at top. Production and validation run simultaneously, not sequentially. Eligibility criteria gate entry at contributor level. | Any community-participatory data collection effort where quality cannot be assumed from contributors and real-time correction is required. |
| **Open-source voice AI orchestration platform (VoiceErA / DPG)** | LLM-agnostic, ASR-agnostic, telephony-provider-agnostic orchestration layer. Supports pluggable component architecture. Hosted on national GPU infrastructure (Bhashini/AI4Bharat). Open source, deployable by government departments and social sector without building from scratch. | Any government or social sector voice AI deployment that cannot afford to build orchestration infrastructure and needs to avoid vendor lock-in. |
| **Bilingual domain sentence corpus (Dehvali Bhili — agricultural and general)** | 25,000 agricultural sentences + 15,000 non-agricultural sentences + 60 hours spontaneous speech + studio and conversational audio. Validated, open-access, hosted on Bhashini. | Any deployer building ASR/TTS/MT for Dehvali Bhili or extending MahaVISTAAR to this language community. Directly reusable without recollection. |

---

## 3. Governance Artifacts

| Artifact | What it is | Reuse condition |
|---|---|---|
| **Ethical compensation model for community data contributors** | Framework for fair, transparent, verified-contribution-based payment to community data contributors. Payments tied to verified task completion, transferred directly to registered accounts. Anonymised participation with unique registration codes. | Any participatory data collection effort involving community members who must be compensated for contribution. |
| **Community trust-building protocol** | Three-step process: (1) explain purpose and data use through repeated field visits and open Q&A before any collection begins; (2) build ownership through public events, community naming of the effort, and open forums; (3) define roles clearly — specific dialect contributors only, elders as anchors, youth as validators. Documented in Astitva booklet. | Any deployment requiring community participation in data creation, especially in tribal or low-literacy populations with prior reason to distrust data collection by government or external actors. |
| **Multi-actor ecosystem map for low-resource language deployment** | Template identifying all required actor roles: convening authority, community speakers, annotators, linguistic validators, data collection platform provider, model builder, hosting infrastructure, application deployer, neutral orchestrator, domain advisors. Each role, what they contribute, and what gaps exist if they are absent. | Any district or state initiating a low-resource language AI effort. Prevents the common failure of starting collection without the full actor set in place. |

---

## 4. Gaps — Information Not in the Source Documents

1. What specific change in a farmer's life would tell you, at twelve months, that this worked — not that the system was used, but that it made a difference?
2. Who owns the Dehvali Bhili dataset? Under what terms was it published to Bhashini — are there restrictions on commercial use? Does the community have any mechanism to withdraw or restrict it?
3. How was Astitva funded? What did it cost? Who bears the ongoing cost of maintaining the language capability in MahaVISTAAR?
4. Before data collection started, what formal agreements existed between the District Administration and external partners? Were there MOUs or data sharing agreements, or was it informal?
5. Who is responsible for the Dehvali Bhili capability in MahaVISTAAR today when it degrades or needs updating?
6. If a farmer receives wrong information from the system, what is the path from that error to a fix?
7. Were there any legal or policy constraints — DPDP, tribal data rights, procurement rules — that you had to comply with as part of the voice data collection?
