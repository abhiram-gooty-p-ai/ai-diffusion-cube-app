# MahaVistaar — Pathway

**Deployment:** MahaVistaar Agricultural Advisory System
**Contributor:** EkStep Foundation / Department of Agriculture, Government of Maharashtra
**Sector:** Agriculture
**Geography:** Maharashtra, India
**Actor type:** Government
**Journey stage:** Scaling
**Dimensions covered:** A, B, C, D, E, F
**Horizontal or vertical:** Vertical (sector-specific)
**Deployment status:** Active
**Last updated:** 2026-06-02
**Contact for peer connection:** EkStep Foundation / OpenAgriNet

## Summary

MahaVistaar is an AI-powered agricultural advisory system deployed by the Department of Agriculture, Government of Maharashtra, serving the state's 1.5 crore farmers through voice telephony, push notifications, chat, and app in Marathi, Hindi, Bhili, and English. Built from commitment to live system in nine months — without an existing playbook, governance framework, or failure mode library — it reached 342,000+ unique users, answered 1.67 million+ farmer questions, and generates 17 lakh daily proactive personalised voice alerts. As the founding deployment of the OpenAgriNet (OAN) digital public goods architecture, this pathway documents how a state government joins fragmented institutional data systems into a voice-first AI advisory service, the economics of migrating from commercial to self-hosted LLM serving, and the institutional sequencing that enabled a nine-month delivery timeline.

---

## A — Problem Orientation

*What you build on.*

**Who were you trying to serve, and what specific problem were you solving for them?**
The deployment targets Maharashtra's 1.5 crore farmers, predominantly smallholders, who faced a structurally fragmented advisory landscape. The state had agricultural university knowledge bases, weather services from IMD, market price data from 307 APMCs, and 40+ government scheme portals — all operating in isolation, none accessible to a farmer through a single point. The problem was not a lack of institutional knowledge but the complete absence of any route for a farmer in the field to reach it.

**What were the access constraints of your users — language, literacy, connectivity — and how did that shape what you built?**
Farmers in Maharashtra communicate across Marathi, Hindi, Bhili, and English, and many have low digital literacy and limited or no smartphone access. The interface layer was built voice-first — accessible over basic telephony — with Bhashini ASR and TTS components handling spoken input and output across all four languages. Multi-channel access was added to serve users with varying device capability, but voice-over-telephony was the non-negotiable inclusion baseline: any farmer who can make a phone call can reach the system.

**Was there data already available to start with, or did you have to build or collect it first?**
The data existed — in agricultural university knowledge bases, IMD weather services, APMC price feeds, farmer registries in AgriStack, and scheme portals in MahaDBT — but it was fragmented across institutions with no shared route to the farmer. Rather than migrating this data into a central repository, the deployment adopted a federated architecture: the AI connects to each institutional source at query time, with each institution retaining ownership of its own data. This preserved data sovereignty and avoided the compliance and institutional cost of centralised migration.

**Why did this problem need AI — what would a non-AI solution have missed?**
The extension officer network in Maharashtra cannot deliver personalised, timely advice to 1.5 crore farmers at the cadence farming decisions require. A non-AI advisory system hits a hard ceiling at the number of human officers available. AI enables thousands of concurrent voice queries to be handled simultaneously — each drawing from multiple real-time institutional sources — and enables a shift from reactive advisory (farmers call in with questions) to proactive advisory (the system sends targeted alerts, such as pest warnings or sowing guidance, before farmers ask).

**Did users interact through voice, an app, or something else — and what drove that choice?**
Users interact through four channels: push notifications, push telephony/IVR, chat/app, and phone. The voice channel over basic telephony was the primary design driver — it reaches farmers regardless of smartphone ownership, data plan availability, or digital literacy. Text and app channels serve users with higher device access. All four channels converge downstream into the same AI processing pipeline, so the underlying system does not differentiate by access mode.

**Did your understanding of the problem change after you started — and if so, how?**
The OAN source documentation records that Maharashtra absorbed nine months of operational learning — including "dialect variation, API instability, trust-building with farmers" — that no subsequent deployment had to rediscover. The system evolved from reactive query-answering toward proactive personalised advisory: the 17 lakh daily proactive voice alerts delivered at scale indicate that farmers needed intelligence pushed to them before they knew to ask, not only responses to questions they had already formulated.

**Is there anything about your users you assumed early on that turned out to be wrong?**
Not documented.

---

## B — Architecture

*What you build with.*

**Did you bring data together into one place or connect to it where it lived — and why?**
Data remains federated. The AI connects to each institutional source at the moment of query — IMD and Skymet for weather, AgriStack and land records for farmer identity and farm data, MahaDBT and scheme databases for government schemes and status, soil labs, KVKs and Kisan Call Centre for extension services, and APMC price feeds for market data. The OAN architecture explicitly frames this as a design commitment: "each institution retains ownership of its own data... the AI connects to data sources at the moment of query, with the farmer's consent, and returns results that cite their institutional origin."

**How did you keep data from multiple sources current and consistent in production?**
Real-time API connections at query time, rather than pre-copied datasets, are the primary consistency mechanism. Weather station coverage presented a documented gap: some rural locations lack nearby monitoring stations, requiring expanded search radii to find the nearest available data point — a tiered search strategy with a defined radius limit. Other consistency mechanisms beyond real-time API connection are not documented.

**What did you build yourself versus use something that already existed?**
Built: the OAN DPG layer (reusable open-source architecture), a fine-tuned Qwen3.5-27B agricultural advisory model, the seven-layer system architecture, and the deployment-specific configuration for Maharashtra (crops, schemes, language). Used existing: Bhashini ASR and TTS (AI4Bharat), voice data from Karya, ICAR knowledge repositories, Beckn protocol for ecosystem interoperability, and the state agricultural data infrastructure already held by the Department of Agriculture and its universities.

**How did you avoid being locked into a single vendor?**
The OAN DPG layer separates the reusable open-source architecture from the Maharashtra-specific deployment configuration, so the base architecture is not bound to any vendor or model. The primary LLM was migrated from Azure OpenAI (GPT-4.1) to a self-hosted fine-tuned Qwen3.5-27B on four H100 GPUs running vLLM with tensor parallelism at TP=4, reducing per-query LLM cost from approximately ₹9.4 to ₹0.05. The Beckn protocol ensures ecosystem interoperability without locking into any single partner's standards.

**Were there sovereign or policy guidelines that shaped your technology choices — around data residency, permitted vendors, or infrastructure?**
NIC (National Informatics Centre) hosting is identified in the architecture documentation as a potential compliance pathway for government deployers whose data residency requirements preclude commercial cloud. The federated architecture — where institutional data stays within each institution's own systems — aligns structurally with data sovereignty requirements without requiring centralisation. Whether specific NIC hosting arrangements have been formalised for this deployment is not documented.

**Did any data source or system integration turn out to be harder than expected?**
Weather station coverage gaps were a documented integration challenge: some rural locations lack nearby monitoring stations, requiring expanded search radii to find the nearest available data point, introducing latency and accuracy trade-offs for weather queries in affected areas. The OAN source document also records that nine months of operational learning included "API instability," implying that at least some data source connections required ongoing reliability management — but specific incidents are not detailed.

**Did the AI ever give a wrong or harmful answer to a user — and how did you catch and handle it?**
The system is built around a dual-model architecture: the primary fine-tuned Qwen3.5-27B advisory model and an independent GPT-OSS Safeguard 20B moderation model that evaluates every output before delivery. The moderation model is fully decoupled from the advisory model — it cannot be influenced by the same prompt injection that might affect the primary model. Specific incidents of wrong or harmful answers reaching users are not documented in available source material.

**What did you put in place to prevent the AI from causing harm — and was it ever tested?**
The independent GPT-OSS Safeguard 20B moderation model runs on every response before the user receives it. It classifies queries as Valid Agricultural, Non-Agricultural, Unsafe/Harmful, or Policy-Sensitive, and performs domain validation, content safety filtering, prompt injection defence, and input sanitisation. In voice channels, moderation is embedded within the ASR pipeline rather than as a separate call. The moderation system operates against an adversarial test set of 500 attack patterns covering prompt injection, hallucination triggers, and jailbreak attempts. The 6,000-token system prompt encodes guardrails including escalation paths directing the AI to refer a farmer to a human officer rather than attempt an answer in cases outside its scope. Whether formal red-team testing beyond the 500-pattern adversarial set has been conducted is not documented.

### Additional Insights

The seven-layer architecture — user, interface, moderation, AI decision engine, knowledge and scientific models, live data and institutional sources, DPI foundation — functions as a reusable deployment template. Each layer has a defined responsibility boundary. This separation allowed the Amul Sarlaben deployment to reuse the architecture in three weeks by substituting cooperative-specific configuration at the interface and data layers without rebuilding the moderation or decision engine layers.

The fine-tuned Qwen3.5-27B model achieved 94% accuracy on the deployment's agricultural advisory evaluation framework, against 91% for larger commercial models. This demonstrates that fine-tuning a smaller open-weight model on domain-specific data can outperform larger general-purpose commercial models while enabling an approximately 188× reduction in per-query LLM cost on the self-hosted serving path.

The serving architecture's concurrency is a VRAM story, not a compute story. A 27B-parameter model in FP16 occupies approximately 54GB of weights, leaving approximately 26GB for KV cache on a single H100 80GB GPU — enough for roughly twelve long-context requests in flight. Tensor parallelism at TP=4 shards model weights across four GPUs, pooling approximately 260GB of KV cache and enabling 80–100 concurrent requests. For a model of this size, TP level is the primary lever that determines unit cost economics.

Prefix caching of the 6,000-token system prompt skips approximately 37% of notional input compute across a typical three-turn advisory session. In the November 2025 Azure spend, input tokens constituted 79.7% of the total LLM bill (output was 5.6%), making prefix caching the most significant cost lever after model choice itself.

---

## C — Institution

*Who deploys AI.*

**How did you get the deployment approved and funded — and did you position it as a one-time project or a long-term transformation initiative?**
The deployment is positioned as a long-term transformation of the state extension delivery system, not a pilot project. The first concrete decision recorded in OAN documentation was nominating an Agri Secretary as institutional sponsor, preceding any technology choice. Nodal officers were nominated across agriculture, IT, and field operations. Gates Foundation, World Bank, and UNDP are named as funders in ecosystem documentation. The specific budget allocation mechanism and formal approval pathway within the Government of Maharashtra are not documented.

**Was there internal resistance — and if so, what actually changed minds?**
Not documented.

**Did you need multiple departments or agencies to cooperate — and where did that get difficult?**
The deployment required data-sharing cooperation across the state agriculture department, the extension directorate, weather services, market data systems, scheme delivery platforms (MahaDBT), and four state agricultural universities. The OAN source document records that "aligning data-sharing across universities, weather services, market data systems, and scheme delivery platforms" was the system leadership work that made everything else possible. Specific inter-departmental friction points and how they were resolved are not documented beyond this framing.

**Did procurement rules create a barrier — and if so how did you get through them?**
Not documented.

**When something went wrong, who was accountable — and was that clear from the start?**
Not documented.

**What happens to this deployment if the key person driving it moves to a different role?**
Not documented.

**Was there a leadership or political change during the deployment, and how did it affect things?**
Not documented.

### Additional Insights

The OAN source documentation identifies the sequencing of the first decision as a transferable lesson: the Agri Secretary sponsor was nominated — with nodal officers across agriculture, IT, and field operations — before any technology or data choices were made. The documented reasoning is that deployments without named public ownership cannot unblock the data-sharing and procurement barriers that require senior political authority to resolve. For a next adopter, the question of who holds named institutional authority over the deployment is the first question to answer, not a question to defer until after technical scope is defined.

---

## D — Ecosystem

*Who executes.*

**How many organisations had to work together for this to function?**
The OAN ecosystem map identifies 54 named enablers across four layers: institutional and governance (funders, orchestrators, government bodies including the Department of Agriculture Maharashtra, Department of Livestock, Department of Fisheries, GoI Ministry of Agriculture, DC Nandurbar, and MahaDBT), technology and AI (IIT Mumbai, IISc, Vassar Labs, India AI Mission, AI4Bharat/Bhashini, Karya, ICAR), structured data (APMC price data, WDRA warehouse data, KVKs, IMD forecast data, Skymet, officer data, scheme data), and knowledge and documents (state programme guidelines, crop knowledge from three agricultural universities, livestock and animal husbandry manuals, fisheries guidelines, national research reports). Named funders are Gates Foundation, World Bank, and UNDP.

**Who was ultimately responsible for keeping all of them aligned — and what did that role actually involve?**
EkStep Foundation holds the network orchestrator role. The role involves maintaining the OAN DPG layer so all deployments can reuse it without rebuilding, coordinating the technology partner ecosystem (including AI4Bharat/Bhashini for language infrastructure and Karya for voice data), and supporting the government deployer in the institutional coordination required to activate federated data-sharing agreements across multiple institutions.

**Were there situations where partners had competing mandates or priorities — and how were those resolved?**
Not documented.

**Did any partner relationship not work out as expected — what happened and how did you handle it?**
Not documented.

**How was trust maintained across partners — especially when something went wrong?**
Not documented.

### Additional Insights

The OAN source documentation frames the ecosystem design principle as: "OpenAgriNet does not build what already exists. It connects it." The 54 enablers predate MahaVistaar — each was a separate system serving a separate purpose with no shared route to the farmer. What OAN contributed was a common network layer allowing these systems to be discovered, combined, and delivered as a coherent response to a single farmer query. For a next adopter, the feasibility question shifts from "what do we need to build?" to "what already exists in this context that can be connected, and under what governance?"

---

## E — Workforce

*Who absorbs AI.*

**Were there people — field workers, extension officers, call centre staff — whose job changed because of this deployment?**
The deployment operates alongside Maharashtra's existing extension officer hierarchy: Krishi Sahayaks (village-level), Block Officers, Sub-Divisional Officers, District Officers, Subject Matter Specialists, and ATMA (Agricultural Technology Management Agency) staff. The AI handles routine advisory queries that previously required a farmer to reach an extension officer by phone or in person. The extension officer role shifts toward cases the AI escalates and toward verification and follow-up rather than first-line query handling.

**How and when were they brought in, and what did they need to learn?**
Farmers were not trained in the conventional sense. The voice interface requires no digital literacy — any farmer who can make a phone call can use the system. The OAN source documentation records that farmers begin naturally with simple queries (mandi prices, weather forecasts) and progress to more complex advisory interactions (crop-specific pest management, scheme eligibility) as familiarity with the system grows. Whether extension officers received formal training on the system, and when in the deployment timeline, is not documented.

**Was there resistance from staff — and if so what worked to address it?**
Not documented.

**How did you train staff at scale — especially those in low-connectivity or low-literacy contexts?**
For farmers, the voice interface itself is the onboarding — no formal training session, digital literacy requirement, or device capability is needed before the system is useful. The OAN source documentation frames this as the "training = use" design principle: the interface eliminates the training bottleneck entirely for the end user. Extension officer training methodology is not documented.

**After the deployment, could staff still do their job if the system was unavailable — or had they become dependent on it?**
Not documented.

### Additional Insights

The "training = use" design principle has a direct consequence for adoption velocity: the deployment can scale as fast as awareness spreads, without a training capacity constraint. Deployments where users must attend a training session, achieve digital literacy, or learn a new interface before first use face a bottleneck that scales linearly with the target population. A voice-over-telephony interface with no prerequisite removes that bottleneck entirely.

---

## F — Operating Model

*What makes it last.*

**What did this cost to build, and what does it cost to run annually?**
The serving architecture internal note documents infrastructure cost in detail. Before migration to self-hosted serving (late 2025), the platform ran on Azure OpenAI (GPT-4.1), accumulating approximately ₹2 lakh per day in LLM spend in November 2025, with the trajectory pointing toward ₹6 lakh per day as Voice AI went live and chatbot adoption scaled. After migration to self-hosted fine-tuned Qwen3.5-27B on four H100 GPUs (vLLM, TP=4): ₹0.05 per question at full utilisation, compared to approximately ₹9.4 per question on Azure — approximately 188× reduction. Actual six-month rental cost of the four-GPU cluster: ₹25 lakh, at approximately ₹144 per GPU-hour (approximately 20% below list price). A planned 16-GPU cluster would cost approximately ₹2 crore per year, against a projected Azure run-rate of approximately ₹18 crore per year at scale. Build cost is not itemised separately in source documentation.

**What did you measure to know it was working — and what did the numbers actually show?**
The deployment tracked query volume by use case, conversational turns per use case, per-query cost, and user feedback ratings. Numbers from the OAN source document: 342,000+ unique users; 1.67 million+ farmer questions answered; 791,000+ sessions, indicating repeat and sustained engagement rather than one-off usage; 17 lakh farmers reached daily through proactive personalised voice alerts; 97%+ positive feedback rate, sustained at 98.5% in the most recent measurement period. Average conversational turns per session by use case — Advisory 3.15, Weather Forecast 2.78, Scheme Information 2.65, Mandi Prices 2.60 — reflect the complexity difference between iterative advisory interactions and single-turn lookups. Outcome measures (improved yields, scheme uptake, farm income) are not documented.

**Who owned operations after the pilot ended, and how was that handover structured?**
The deployment was not framed as a pilot — the OAN source document positions it as a long-term transformation of the extension delivery system. The Department of Agriculture, Government of Maharashtra holds institutional ownership. Operational handover structure is not applicable in the framing of source documentation.

**Was there an outcome or a problem that showed up later that you wished you had been measuring from the start?**
The serving architecture internal note documents that at the time of writing, three key operational metrics were modelled rather than observed: the provider split (fraction of traffic served by self-hosted versus Azure fallback), per-flow latency percentiles (p50/p95/p99 by use case), and the correlation between fallback events and traffic patterns. Langfuse observability integration was provisioned but not yet live at the time of the note. These three gaps are identified explicitly as the measurements needed to responsibly tune the concurrency cap and validate the latency guarantee.

**Was there a point where the whole thing nearly stalled — and what got it through?**
Not documented.

**Were there compliance, audit, or regulatory requirements that shaped how you ran operations?**
NIC hosting is identified as a potential compliance pathway for sensitive data. The architecture documentation includes rate-limiting infrastructure (IP-based throttling, adaptive rate limiting) to defend against denial-of-wallet attacks targeting GPU and token budgets rather than network availability. Whether specific compliance arrangements have been formalised is not documented.

### Additional Insights

Advisory queries consumed 67.2% of total LLM spend in the November 2025 Azure period on 57% of total query volume — a heavier per-question cost (₹11.06 on Azure) than any other use case. This concentration is documented as the reason the serving architecture is tuned to the Advisory worst case: three or more turns, long tool-result payloads, 84,000-token context ceiling, TP=4 for concurrency. Making Advisory cheaper is, effectively, making the entire platform cheaper.

The blended cost per question depends on how often the Azure fallback fires. At the time of the serving architecture note, the 100-concurrent-call cap was set conservatively and spillover was inferred to be rare rather than measured. The ₹0.05 per question figure is a marginal cost at full self-hosted utilisation, not the observed operational blended cost. The practical consequence for a next adopter planning comparable infrastructure: actual blended cost is higher than the self-hosted marginal until observability tooling confirms the real fallback rate.

---

## Reusable Toolkit

| Asset | Type | What it is useful for | How to access |
|---|---|---|---|
| OAN DPG layer | Open-source codebase | Foundational architecture for agricultural AI advisory; reusable across state and country deployments without rebuilding from scratch | Via EkStep Foundation / OpenAgriNet |
| Seven-layer system architecture | Architecture blueprint | Designing the full stack from user interface to DPI foundation for an AI advisory system | Documented in OAN Diffusion Pathway source materials |
| Fine-tuned Qwen3.5-27B model | LLM weights | Agricultural advisory in Indian languages; starting point for fine-tuning in new geographies | Availability via public release not confirmed in source documentation |
| vLLM TP=4 serving configuration | Infrastructure blueprint | Self-hosted LLM serving at scale; concurrency design for 27B-class models on H100 GPU clusters | Documented in MahaVistaar Production Serving Architecture internal note |
| Adversarial test set | Evaluation dataset | 500 attack patterns (prompt injection, hallucination triggers, jailbreak attempts) for evaluating agricultural AI moderation models | Via EkStep Foundation |
| 54-enabler ecosystem map | Ecosystem design template | Identifying the minimum viable partner set for a comparable state-level deployment | Via EkStep Foundation / OAN |
| Governance frameworks and deployment playbooks | Documentation | Institutional alignment templates, data-sharing governance models — produced by Maharashtra and available to subsequent deployers because Maharashtra built without them | Via EkStep Foundation / OAN |
| Beckn protocol integration | Interoperability standard | Connecting ecosystem partners without proprietary lock-in | Beckn protocol community / EkStep Foundation |

---

## Related Pathways

- [Bharat-VISTAAR](bharat-vistaar.md) — National agricultural DPI built on MahaVistaar architecture; MahaVistaar connects as its Maharashtra node
- [Amul Sarlaben](amul-sarlaben.md) — Cooperative dairy deployment reusing OAN DPG layer; deployed in 3 weeks by adapting MahaVistaar's architecture and governance frameworks
- [Bihar Krishi](bihar-krishi.md) — Independent state agricultural platform built on a different path; now connected to Bharat-VISTAAR as Bihar node
- [Ethiopia ATI](ethiopia-ati.md) — First international OAN deployment; deployed in 3 months by adapting Maharashtra's architecture and documented learnings
- [Project Astitva](project-astitva.md) — District-led participatory language AI in Nandurbar that produced Dehwali Bhili voice data now integrated into MahaVistaar

## Related Entities

- [EkStep Foundation](../entities/ekstep-foundation.md)
- [OpenAgriNet](../entities/openagri-net.md)
- [Bhashini / AI4Bharat](../entities/bhashini.md)
- [Karya](../entities/karya.md)

## Lineage

MahaVistaar is the anchor OAN deployment. It was built without an existing playbook, governance framework, or failure mode library. All subsequent OAN deployments — [Bharat-VISTAAR](bharat-vistaar.md), [Amul Sarlaben](amul-sarlaben.md), [Ethiopia ATI](ethiopia-ati.md) — drew on MahaVistaar's architecture, code, governance frameworks, and operational learnings.
