# Project Astitva — Pathway

**Deployment:** Project Astitva — Participatory Language AI for Tribal Communities
**Contributor:** District Administration Nandurbar / Karya
**Sector:** Cross-sector (language infrastructure)
**Geography:** Nandurbar District, Maharashtra, India
**Actor type:** Government
**Journey stage:** Pilot
**Dimensions covered:** A, B, C, E
**Horizontal or vertical:** Horizontal (cross-sector function)
**Deployment status:** Active
**Last updated:** 2026-06-02
**Contact for peer connection:** District Administration Nandurbar / Karya

## Summary

Project Astitva is a district-led initiative to build participatory language AI for tribal communities in Nandurbar — a district where 69% of the population are Scheduled Tribes speaking 18+ languages and dialects including Bhili, Pawari, Kokani, and Mavchi. The District Administration of Nandurbar collaborated with Karya (a social enterprise specialising in ethical datasets for underserved communities) to collect agricultural and general speech data from community members in one month, producing a validated open language repository now hosted on Bhashini and integrated into MahaVistaar. This pathway is useful to adopters asking how a district government can build language infrastructure for low-resource languages at speed with community participation, and how language data collection can be designed to be compensated, ethical, and community-owned rather than extracted.

---

## A — Problem Orientation

*What you build on.*

**Who were you trying to serve, and what specific problem were you solving for them?**
The deployment serves over 9 lakh tribal residents of Nandurbar district, where 69% of the population belongs to Scheduled Tribes. The problem is linguistic exclusion from digital public services: AI systems built on dominant languages (Marathi, Hindi, English) do not work in Bhili, Pawari, Kokani, Mavchi, and the other languages and dialects spoken by Nandurbar's tribal communities. "Language is not just a medium of conversation. It's the key to accessing public information and trusting services." Without voice recognition and speech synthesis for these languages, any voice-first AI advisory system — including MahaVistaar — cannot serve a significant share of Maharashtra's tribal population.

**What were the access constraints of your users — language, literacy, connectivity — and how did that shape what you built?**
The primary constraint is language: 18+ languages and dialects across Nandurbar, with the primary written form being either absent or inaccessible to much of the population. This shaped the approach as voice-first and participatory: the community contributes speech data in its own languages, building AI capabilities from the ground up rather than adapting dominant-language systems. The Astitva booklet frames this as "a democratic approach to digital communication, led by the district and built through broad institutional and community collaboration."

**Was there data already available to start with, or did you have to build or collect it first?**
Language data for Bhili, Pawari, Kokani, and Mavchi did not exist at the scale required for AI model training. The entire purpose of Project Astitva was to create this data through participatory community collection — it had to be built from scratch. Agricultural domain sentences were collected first (25,000 sentences) because the primary deployment target was agricultural advisory integration with MahaVistaar.

**Why did this problem need AI — what would a non-AI solution have missed?**
Building voice recognition (ASR) and voice synthesis (TTS) for low-resource tribal languages is not feasible without machine learning — the scale of pattern recognition required cannot be achieved through rules-based or manual systems. Without AI-capable language infrastructure, tribal language speakers are permanently excluded from voice-first digital public services regardless of how well those services are designed in other respects.

**Did users interact through voice, an app, or something else — and what drove that choice?**
The deployment output is language model infrastructure (ASR/TTS), not a user-facing application itself. The infrastructure enables future voice-based interactions for tribal language speakers — in agricultural advisory (MahaVistaar), healthcare (Asha/ANM/AWW bots), education, and administration. Voice was chosen as the output modality because it is the access mode that works for populations with low literacy or no smartphones.

**Did your understanding of the problem change after you started — and if so, how?**
Not documented beyond the general observation that "limited time can increase speed but affect quality" — the month-long intensive collection period required trade-offs between speed and data quality that the team had to manage.

**Is there anything about your users you assumed early on that turned out to be wrong?**
Not documented.

### Additional Insights

The three-phase output from Astitva (agriculture domain → non-agriculture domain → conversational speech) suggests that domain specificity matters in data collection order: agricultural sentences were collected first because the immediate application target was agricultural advisory. A next adopter building language infrastructure for a specific sector deployment should consider starting with the domain vocabulary most relevant to the intended application rather than collecting general-purpose speech data first.

---

## B — Architecture

*What you build with.*

**Did you bring data together into one place or connect to it where it lived — and why?**
The language data collected through Astitva is consolidated into a community language repository, hosted on Bhashini — India's national language AI platform — where it is made openly accessible. Open access enables nationwide adaptability: other districts, departments, or application developers can use the Dehwali Bhili language models without reconstructing the collection effort. The repository is centralised at Bhashini rather than held locally in Nandurbar.

**How did you keep data from multiple sources current and consistent in production?**
The repository is structured for ongoing updates and domain-specific expansions — three additional languages (Mathwadi Bhili, Mavachi, Pawari) were planned at the time of the source booklet. Community ownership of the dataset is positioned as the sustainability mechanism: "Community language repository promotes sustained use."

**What did you build yourself versus use something that already existed?**
All language data was collected from scratch through community participation — no existing ASR/TTS models existed for Bhili and other Nandurbar languages. The Bhashini platform (built by AI4Bharat) provided the hosting and model training infrastructure. Karya provided the ethical dataset collection methodology, including consent design, community compensation, and data quality protocols. The District Administration provided the institutional authority to convene the Tribaldaan conclave with Bhashini and coordinate across departments.

**How did you avoid being locked into a single vendor?**
The data is hosted on Bhashini, a government-backed national language AI platform, and described as "open access" — any downstream application developer can use it. "Transportability to other domains and districts" is documented as a design goal. Ongoing ownership by the tribal department ensures the data is not locked to Karya or any other collection partner.

**Were there sovereign or policy guidelines that shaped your technology choices — around data residency, permitted vendors, or infrastructure?**
Hosting on Bhashini (a Government of India platform) is consistent with data sovereignty requirements for government-collected community data. Strict monitoring and accountability protocols for irregularities are documented. The consent mechanism — community members confirmed participation and data use — is built into the collection design.

**Did any data source or system integration turn out to be harder than expected?**
The primary documented challenge is quality: "limited time can increase speed but affect quality." The one-month intensive collection period was necessary to meet targets but created pressure on data quality. This is presented in the Astitva booklet as a design tension, not a resolved problem — implying that quality monitoring during intensive collection was an active challenge.

**Did the AI ever give a wrong or harmful answer to a user — and how did you catch and handle it?**
Not applicable — Project Astitva produced language infrastructure (ASR/TTS data), not a deployed AI advisory system. Downstream applications using the language models (MahaVistaar, future health bots) carry their own harm prevention mechanisms.

**What did you put in place to prevent the AI from causing harm — and was it ever tested?**
Not applicable in the same sense as AI advisory deployments. The consent mechanism and strict monitoring of data collection irregularities are the primary safeguards documented for the data collection phase.

---

## C — Institution

*Who deploys AI.*

**How did you get the deployment approved and funded — and did you position it as a one-time project or a long-term transformation initiative?**
The District Administration of Nandurbar led the initiative, drawing on delegated financial powers at the district level. The District Collector's authority to head all line departments — and converge Education, IT, Agriculture, and Tribal Welfare — provided the institutional mandate. The Astitva booklet frames this as both a technical project and "a matter of district pride" — institutional pride as a motivational driver alongside technical objectives. Initial district work transitioned to the state level, with ongoing ownership by the tribal department, indicating long-term intent rather than a bounded project.

**Was there internal resistance — and if so, what actually changed minds?**
Not documented.

**Did you need multiple departments or agencies to cooperate — and where did that get difficult?**
The deployment required convergence across Education, IT, Agriculture, and Tribal Welfare departments, coordinated through the District Collector's authority. The Tribaldaan conclave with Bhashini was a specific coordination event that brought community, district, and national platform stakeholders together. Specific inter-departmental friction points are not documented.

**Did procurement rules create a barrier — and if so how did you get through them?**
Not documented. Delegated financial powers at the district level provided procurement flexibility.

**When something went wrong, who was accountable — and was that clear from the start?**
The booklet documents: "Strict monitoring and accountability. Irregularities addressed immediately." The specific accountability structure is not further documented.

**What happens to this deployment if the key person driving it moves to a different role?**
The institutional transition from district administration to state-level ownership, with ongoing ownership by the tribal department, is designed to reduce key-person dependency. The community-owned repository on Bhashini further reduces reliance on any single official's continued involvement.

**Was there a leadership or political change during the deployment, and how did it affect things?**
Not documented.

### Additional Insights

The Astitva booklet articulates a specific institutional argument for district administration leadership over language AI initiatives: "The District Administration is uniquely positioned to bring these stakeholders together and enable synergy between them." The argument is grounded in the District Collector's constitutional authority over all line departments — enabling convergence of Education, IT, Agriculture, and Tribal Welfare data and staff without requiring inter-departmental negotiations at a higher level. For a next adopter designing community language data collection, district-level leadership with delegated financial powers is the institutional configuration the evidence supports, rather than a national-level or NGO-led initiative.

---

## D — Ecosystem

*Who executes.*

**How many organisations had to work together for this to function?**
District Administration Nandurbar as lead; Karya (social enterprise for ethical dataset collection and community compensation); AI4Bharat/Bhashini (national language AI platform as hosting infrastructure); health workers, revenue staff, and community members as data contributors; tribal department as ongoing owner. The Tribaldaan conclave brought community, district, and national platform stakeholders together for a specific trust-building event.

**Who was ultimately responsible for keeping all of them aligned — and what did that role actually involve?**
The District Collector, as head of all line departments, held the coordination authority. In practice: convening the Tribaldaan conclave, authorising participation through district circulars, coordinating data collection across departments and community groups, and managing the transition to state-level ownership.

**Were there situations where partners had competing mandates or priorities — and how were those resolved?**
Not documented.

**Did any partner relationship not work out as expected — what happened and how did you handle it?**
Not documented.

**How was trust maintained across partners — especially when something went wrong?**
The Tribaldaan conclave with Bhashini is the primary documented trust-building mechanism — a formal gathering that brought community, district administration, and the national platform together before data collection began. The Astitva booklet states: "Participation was not assumed. It was designed, facilitated, compensated, and respected." Karya's ethical dataset collection model (community compensation, clear consent) is the specific mechanism that built trust with community contributors.

---

## E — Workforce

*Who absorbs AI.*

**Were there people — field workers, extension officers, call centre staff — whose job changed because of this deployment?**
Health workers and revenue staff were contributors to the data collection effort — their job temporarily expanded to include participatory speech data recording in the collection phase. Community members whose languages were documented became active contributors to the knowledge base rather than passive beneficiaries of AI systems built without their languages.

**How and when were they brought in, and what did they need to learn?**
District circulars from the District Collector authorised participation across departments. The Astitva booklet describes "intensive coordination and sustained motivation" as essential for meeting collection targets within one month. Staff and community members were briefed on the purpose and process of data collection before contributing. Karya's ethical dataset methodology included training on collection protocols.

**Was there resistance from staff — and if so what worked to address it?**
Not documented.

**How did you train staff at scale — especially those in low-connectivity or low-literacy contexts?**
The participatory collection model recruited community members who speak the target languages — they were not learning to use a digital system but contributing speech in their own language. Karya's methodology for ethical community data collection includes protocols for working with contributors who may have low literacy or digital experience. Specific training methods are not documented in the booklet.

**After the deployment, could staff still do their job if the system was unavailable — or had they become dependent on it?**
Not applicable — the deployment produced language data infrastructure, not an operational tool that staff depend on for daily tasks.

### Additional Insights

Karya's compensation model — community members are paid for their participation in data collection — is the mechanism that makes ethical data collection sustainable and respects community members' time. The Astitva booklet makes this explicit: "Participation was not assumed. It was designed, facilitated, compensated, and respected." For a next adopter building language data for underserved communities, compensation is documented as a design requirement, not an optional feature. Uncompensated data collection from marginalised communities produces both ethical problems and lower data quality.

---

## F — Operating Model

*What makes it last.*

**What did this cost to build, and what does it cost to run annually?**
Not documented. Delegated district financial powers funded the initial phase. Ongoing operational costs of maintaining and expanding the language repository are not documented.

**What did you measure to know it was working — and what did the numbers actually show?**
Initial phase outputs (completed within one month): 25,000 agriculture sentences collected; 15,000 non-agriculture sentences collected; 60 hours of spontaneous speech recorded; 6 hours of studio speech recorded; 2 hours of conversational speech recorded. Downstream integration: Dehwali Bhili integrated into MahaVistaar; validated open language repository available on Bhashini. Future use cases enabled: Asha/ANM/AWW Bot, Education, Administration.

**Who owned operations after the pilot ended, and how was that handover structured?**
Work transitioned from district administration to state-level ownership, with the tribal department as ongoing owner. The community language repository on Bhashini is managed as an open resource. The specific handover structure and timeline are not documented.

**Was there an outcome or a problem that showed up later that you wished you had been measuring from the start?**
Not documented.

**Was there a point where the whole thing nearly stalled — and what got it through?**
The booklet documents that "intensive coordination and sustained motivation were essential for meeting targets" — implying that motivation maintenance was an active operational challenge during the one-month intensive collection period.

**Were there compliance, audit, or regulatory requirements that shaped how you ran operations?**
Community consent for data use is documented as a core protocol. Strict monitoring of irregularities and immediate corrective action is documented. Specific regulatory requirements are not documented.

---

## Reusable Toolkit

| Asset | Type | What it is useful for | How to access |
|---|---|---|---|
| Dehwali Bhili language model | ASR/TTS model | Voice recognition and synthesis for Dehwali Bhili; enables tribal language voice AI applications | Bhashini platform (open access) |
| Community data collection methodology | Process template | Participatory, compensated, consent-based speech data collection for underserved languages; applicable to other tribal or low-resource language contexts | Via Karya / District Administration Nandurbar |
| Tribaldaan conclave model | Governance template | Trust-building event design for bringing community, government, and national platform stakeholders together before data collection | Via District Administration Nandurbar |

---

## Related Pathways

- [MahaVistaar](mahavistaar.md) — Agricultural advisory system that integrated Dehwali Bhili voice capabilities produced by Project Astitva; provided institutional support to Astitva during implementation

## Related Entities

- [Karya](../entities/karya.md)
- [Bhashini / AI4Bharat](../entities/bhashini.md)

## Lineage

Not documented. Project Astitva was initiated by District Administration Nandurbar independently; it became an enabling project for [MahaVistaar](mahavistaar.md) rather than drawing on MahaVistaar's lineage.
