# Amul Sarlaben — Pathway

**Deployment:** Amul Sarlaben Dairy Advisory System
**Contributor:** EkStep Foundation / Amul (Gujarat Cooperative Milk Marketing Federation)
**Sector:** Agriculture (Dairy)
**Geography:** Gujarat, India (18,500+ villages)
**Actor type:** Cooperative
**Journey stage:** Scaling
**Dimensions covered:** A, B, C, D, E
**Horizontal or vertical:** Vertical (sector-specific)
**Deployment status:** Active
**Last updated:** 2026-06-02
**Contact for peer connection:** Amul (Gujarat Cooperative Milk Marketing Federation) / EkStep Foundation

## Summary

Amul Sarlaben is an AI-powered dairy advisory system deployed by Amul — the world's largest dairy cooperative — placing personalised animal health, feeding, breeding, and scheme information in the hands of 3.6 million women milk producers across 18,500+ villages in Gujarat through voice calls in Gujarati on feature phones and landlines. The deployment went from commitment to live system in three weeks — the fastest OAN deployment documented — because it could adapt the architecture, governance frameworks, and deployment playbooks produced by MahaVistaar's nine-month founding effort rather than building them. This pathway is useful to adopters asking how a cooperative with deep existing data infrastructure can add an AI advisory layer for its members, how institutional trust can substitute for government authority, and what three-week deployment actually requires.

---

## A — Problem Orientation

*What you build on.*

**Who were you trying to serve, and what specific problem were you solving for them?**
The deployment serves Amul's 3.6 million milk producers — predominantly women — across 18,500+ villages in Gujarat. Despite Amul processing 3.5 crore litres of milk daily and maintaining 50 years of cooperative transaction records, individual producers had never had direct access to the knowledge held in Amul's own data: 2 billion milk procurement transactions, records on 30 million cattle, 1,200+ veterinary doctors' records, and half a century of cooperative history. The data existed and had never spoken back to the farmer who generated it.

**What were the access constraints of your users — language, literacy, connectivity — and how did that shape what you built?**
The primary users are women dairy producers, many of whom have never had a smartphone. The OAN source document notes: "For many dairy farmers — and in particular for the women who form the majority of cooperative dairy producers in some regions — a voice call in their own language is the only channel that works." Sarlaben delivers through voice in Gujarati, reachable by feature phone and landline. The system speaks to users in the language they actually speak, through the device they actually have. Planned expansion to 20 Indian languages via Bhashini indicates that language access is a design priority rather than an afterthought.

**Was there data already available to start with, or did you have to build or collect it first?**
Amul's cooperative data infrastructure was the entire foundation: 2 billion milk procurement transactions, records on 30 million cattle each with a unique ID tracking feed, health, treatment, and milking history, 1,200+ veterinary doctors contributing records annually, and 50 years of cooperative operational history. The constraint was not data availability but the absence of any mechanism for an individual farmer to access the intelligence this data could generate. The deployment required an AI layer, not a data collection effort.

**Why did this problem need AI — what would a non-AI solution have missed?**
Amul has approximately 1,400 veterinary doctors serving 3.6 million farmers and 22 million cattle — a ratio that makes personalised advisory through human professionals structurally impossible at the frequency farmers need it. A non-AI solution could not reach an individual farmer on a feature phone at any hour with advice specific to their individual animal's health records, reproductive history, and feeding profile. The key word is individual: generic livestock advisory existed before Sarlaben; what AI enables is advisory grounded in the specific animal the farmer is standing next to.

**Did users interact through voice, an app, or something else — and what drove that choice?**
Voice in Gujarati through feature phone and landline is the primary access channel. One million+ app downloads are documented, indicating a parallel app channel for users with smartphones. The voice channel design was driven by the need to reach women dairy producers who have never had a smartphone and may not read with ease — the access profile of the primary user determined the primary channel.

**Did your understanding of the problem change after you started — and if so, how?**
Not documented.

**Is there anything about your users you assumed early on that turned out to be wrong?**
Not documented.

---

## B — Architecture

*What you build with.*

**Did you bring data together into one place or connect to it where it lived — and why?**
The cooperative's institutional data remains in the cooperative's systems. The AI connects to it at query time. The OAN source document describes the design explicitly: "the cooperative's institutional data remains in the cooperative's systems. The AI reaches it, assembles the answer, and delivers it in Gujarati through a voice call to a feature phone. The institution did not change." This is the same federated principle as MahaVistaar, applied to a cooperative data context rather than a government data context.

**How did you keep data from multiple sources current and consistent in production?**
Not documented. The cooperative's transaction and animal health records are maintained within Amul's own operational systems; the AI layer reads from these rather than maintaining a separate copy.

**What did you build yourself versus use something that already existed?**
Sarlaben reused the OAN DPG layer, architecture, governance frameworks, and deployment playbooks produced by MahaVistaar — adapting them to a cooperative context, a Gujarati language context, and a dairy-specific data foundation rather than rebuilding any of these from scratch. The OAN source document identifies the three-week deployment time as a direct consequence of this reuse: "the architecture, governance frameworks, and deployment playbooks had already been built by Maharashtra and did not need to be rebuilt."

**How did you avoid being locked into a single vendor?**
The same OAN DPG layer and Beckn protocol mechanisms as MahaVistaar. Planned expansion via Bhashini for multilingual access reinforces language-layer independence. Specific vendor-independence measures beyond the shared OAN architecture are not documented.

**Were there sovereign or policy guidelines that shaped your technology choices — around data residency, permitted vendors, or infrastructure?**
Not documented. As a private sector cooperative, different constraints apply than for government deployers; specific cooperative data governance requirements that shaped technology choices are not documented.

**Did any data source or system integration turn out to be harder than expected?**
Not documented.

**Did the AI ever give a wrong or harmful answer to a user — and how did you catch and handle it?**
Not documented.

**What did you put in place to prevent the AI from causing harm — and was it ever tested?**
Not documented beyond the shared OAN architectural moderation layer.

### Additional Insights

The dairy advisory use cases documented in the OAN source are individually structured: the system draws from a specific animal's records — not from a generic livestock database — to answer questions about that animal's health, feeding, reproductive cycle, and treatment history. This individual-level advisory, grounded in the unique animal ID that Amul maintains for each of its 30 million cattle, is what differentiates Sarlaben from generic agricultural AI and what required the cooperative's data infrastructure as a foundation. A government or NGO without this pre-existing individual-animal data layer would face a substantially different data preparation challenge.

---

## C — Institution

*Who deploys AI.*

**How did you get the deployment approved and funded — and did you position it as a one-time project or a long-term transformation initiative?**
Not documented in detail. Amul as a private sector cooperative operates under different approval and funding mechanisms than a government deployer. The three-week deployment timeline implies a streamlined internal decision process rather than a lengthy government approval pathway. The planned expansion to 20 Indian languages and 20,000+ villages indicates long-term framing.

**Was there internal resistance — and if so, what actually changed minds?**
Not documented.

**Did you need multiple departments or agencies to cooperate — and where did that get difficult?**
The cooperative context made this structurally simpler than government deployments: "the data infrastructure, the institutional relationships, and the member trust had all been built over 50 years of cooperative transactions." Amul's internal data ownership meant that inter-institutional data-sharing negotiations — the primary source of institutional friction in government deployments — were not required. The AI layer needed to connect to Amul's own systems, not negotiate access across agencies.

**Did procurement rules create a barrier — and if so how did you get through them?**
Not documented. Private sector procurement operates differently from government procurement, and specific barriers are not documented.

**When something went wrong, who was accountable — and was that clear from the start?**
Not documented.

**What happens to this deployment if the key person driving it moves to a different role?**
Not documented.

**Was there a leadership or political change during the deployment, and how did it affect things?**
Not applicable — private sector cooperative context.

### Additional Insights

The three-week deployment is the fastest documented on the OAN pathway. The OAN source document attributes this directly to what Amul did not need to build: "Amul adapted them to its cooperative context, its data foundation, and its members" — rather than constructing the architecture, governance frameworks, and deployment playbooks from scratch. For a next adopter with an existing data infrastructure and internal institutional trust (as opposed to multi-agency government coordination), the investment required to reach a live system is substantially compressed once the architectural building blocks exist. The constraint shifts from construction to adaptation.

---

## D — Ecosystem

*Who executes.*

**How many organisations had to work together for this to function?**
The cooperative context means Amul is largely self-contained for data and institutional authority. EkStep Foundation provided the OAN DPG layer and pathway know-how. AI4Bharat/Bhashini provides language infrastructure for Gujarati voice access. The smaller ecosystem footprint — compared to MahaVistaar's 54-enabler map — reflects that Amul's cooperative data was internally held and did not require external data-sharing agreements.

**Who was ultimately responsible for keeping all of them aligned — and what did that role actually involve?**
Not documented in detail. EkStep Foundation's network orchestrator role extends to Amul Sarlaben as an OAN deployment.

**Were there situations where partners had competing mandates or priorities — and how were those resolved?**
Not documented.

**Did any partner relationship not work out as expected — what happened and how did you handle it?**
Not documented.

**How was trust maintained across partners — especially when something went wrong?**
Not documented.

---

## E — Workforce

*Who absorbs AI.*

**Were there people — field workers, extension officers, call centre staff — whose job changed because of this deployment?**
Amul's 1,400+ veterinary doctors are the professional advisory workforce whose relationship to members the deployment changes. The AI provides a first line of advisory that is accessible at any hour; the vet workforce handles cases the AI escalates and provides the professional knowledge that the AI's advisory corpus draws from. The OAN source document notes that 1,200+ veterinary doctors contribute records annually — making them contributors to the knowledge base the system draws on, not just advisors displaced by it.

**How and when were they brought in, and what did they need to learn?**
Not documented.

**Was there resistance from staff — and if so what worked to address it?**
Not documented.

**How did you train staff at scale — especially those in low-connectivity or low-literacy contexts?**
For farmers: the same "training = use" design principle as MahaVistaar applies. The OAN source document describes farmers reaching the system "through a call, in their language, at any hour" without a training prerequisite. The questions farmers are asking — about a sick animal, feeding, vaccinations — are "the same questions they have always had." What changed is that there is now a system that can answer them. No formal training or digital literacy is required to make a voice call.

**After the deployment, could staff still do their job if the system was unavailable — or had they become dependent on it?**
Not documented.

---

## F — Operating Model

*What makes it last.*

**What did this cost to build, and what does it cost to run annually?**
Not documented.

**What did you measure to know it was working — and what did the numbers actually show?**
At launch: 3.6 million farmers reached; 1 million+ app downloads. Referenced by Prime Minister Modi at the India AI Impact Summit 2026. Further engagement metrics (session volume, query breakdown, feedback rates) are not documented in available source material.

**Who owned operations after the pilot ended, and how was that handover structured?**
Not documented. Amul as the deploying cooperative is the institutional owner.

**Was there an outcome or a problem that showed up later that you wished you had been measuring from the start?**
Not documented.

**Was there a point where the whole thing nearly stalled — and what got it through?**
Not documented.

**Were there compliance, audit, or regulatory requirements that shaped how you ran operations?**
Not documented.

---

## Reusable Toolkit

No reusable assets documented separately from the OAN DPG layer. The three-week deployment demonstrates the value of what can be reused; see [MahaVistaar Reusable Toolkit](mahavistaar.md#reusable-toolkit) for the shared architectural assets.

---

## Related Pathways

- [MahaVistaar](mahavistaar.md) — Anchor OAN deployment; architecture, governance frameworks, and playbooks reused for Amul's three-week deployment
- [Bharat-VISTAAR](bharat-vistaar.md) — National layer that connects Amul Sarlaben (identified as "Gujarat through Amul AI") alongside state nodes
- [Bihar Krishi](bihar-krishi.md) — Government state deployment for comparison; different institutional context, similar federated architecture approach

## Related Entities

- [EkStep Foundation](../entities/ekstep-foundation.md)
- [OpenAgriNet](../entities/openagri-net.md)
- [Amul](../entities/amul.md)
- [Bhashini / AI4Bharat](../entities/bhashini.md)

## Lineage

Built on [MahaVistaar](mahavistaar.md) — architecture, governance frameworks, and deployment playbooks adapted to cooperative context; "what Maharashtra built, Amul adapted."
