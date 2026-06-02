# Bharat-VISTAAR — Pathway

**Deployment:** Bharat-VISTAAR (Versatile Intelligent Solutions for Transforming Agriculture and Allied Rural economies)
**Contributor:** EkStep Foundation / Ministry of Agriculture and Farmers Welfare, Government of India
**Sector:** Agriculture
**Geography:** India (national)
**Actor type:** Government
**Journey stage:** Pilot
**Dimensions covered:** A, B, C
**Horizontal or vertical:** Vertical (sector-specific)
**Deployment status:** Active
**Last updated:** 2026-06-02
**Contact for peer connection:** Ministry of Agriculture and Farmers Welfare, Government of India / EkStep Foundation

## Summary

Bharat-VISTAAR is India's national digital public infrastructure for agriculture — analogous to UPI for payments, extended to agricultural information and services. Announced in the Union Budget 2026-27 with an allocation of Rs. 150 crore and formally launched on 17 February 2026, it operates as the common rail connecting state and cooperative agricultural AI deployments (Maharashtra's MahaVistaar, Gujarat's Amul Sarlaben, Bihar's Bihar Krishi) with national knowledge resources, the AgriStack farmer registry, and PM scheme connectivity. As a pathway, Bharat-VISTAAR is useful to adopters asking how a national government can act as an integrator — amplifying what states have already built rather than replacing it — and how to establish federated national AI infrastructure across a country with 120 million farmers and dozens of languages.

---

## A — Problem Orientation

*What you build on.*

**Who were you trying to serve, and what specific problem were you solving for them?**
The deployment targets India's 120 million farmers across dozens of states, languages, crop systems, and agricultural contexts. The problem is structural: no single state platform can reach all of them, and fragmented state-level deployments cannot share knowledge infrastructure (ICAR advisory corpus, national pest surveillance, PM scheme data) or reach farmers who migrate between states. The national architecture provides the common rail on which state and cooperative platforms connect as nodes, each retaining local specificity while drawing on national coherence.

**What were the access constraints of your users — language, literacy, connectivity — and how did that shape what you built?**
Phase 1 launched with feature phone access via 155261 in Hindi and English. Full multilingual expansion — to serve farmers across the country in their own languages — is a stated trajectory via Bhashini, but the breadth of language coverage at the point of launch is not documented beyond Hindi and English. Connectivity constraints faced by rural farmers across India are addressed by maintaining voice and feature phone access rather than requiring smartphones or broadband.

**Was there data already available to start with, or did you have to build or collect it first?**
The national layer draws on existing institutional data: AgriStack (national farmer registry), the ICAR advisory corpus (national agricultural research knowledge), IMD weather data, NPSS (National Pest Surveillance System) alerts, and the data infrastructure of connected state nodes (MahaVistaar for Maharashtra, Bihar Krishi for Bihar). The design principle is integration, not replication: the national layer provides connectivity to sources that already exist, not a new centralised data store.

**Why did this problem need AI — what would a non-AI solution have missed?**
India's agricultural advisory landscape is too fragmented for any non-AI coordination mechanism to address at national scale in real time. AI enables a farmer to speak a question in their own language and receive a response that synthesises simultaneously from national-level resources (ICAR, national pest alerts, PM scheme databases) and state-level sources (local mandi prices, district extension officer contacts) in a single conversational exchange. Without AI, these sources remain siloed even if connectivity infrastructure exists.

**Did users interact through voice, an app, or something else — and what drove that choice?**
Feature phone access via short code 155261 in Hindi and English was the Phase 1 delivery channel. The choice of feature phone voice access — not smartphone or broadband — reflects the inclusion principle consistent across OAN deployments: the system must be reachable by farmers who have only a basic phone.

**Did your understanding of the problem change after you started — and if so, how?**
Not documented. Bharat-VISTAAR was very recently launched at the time of source documentation (February 2026).

**Is there anything about your users you assumed early on that turned out to be wrong?**
Not documented.

---

## B — Architecture

*What you build with.*

**Did you bring data together into one place or connect to it where it lived — and why?**
The national layer connects to data where it lives — in state systems, national registries, and research institutions — rather than consolidating it. The OAN source document describes Bharat-VISTAAR as providing "the shared knowledge base, the AgriStack integration, the ICAR advisory corpus, and the PM scheme connectivity that no single state could build alone." State nodes (MahaVistaar, Bihar Krishi, Amul Sarlaben) connect to the national layer and through it to these national resources, while their own local data remains in state systems.

**How did you keep data from multiple sources current and consistent in production?**
Not documented. The deployment was newly launched at the time of source documentation.

**What did you build yourself versus use something that already existed?**
Bharat-VISTAAR is described as built on the OAN architecture established by MahaVistaar. The national layer provides the integration infrastructure — AgriStack connectivity, ICAR advisory corpus access, PM scheme connectivity — on top of the existing OAN DPG building blocks. The Saagu Baagu pilot in Telangana is identified as an antecedent whose design informed Bharat-VISTAAR's approach; that pilot showed 21% increase in yield per acre and 9% reduction in pesticide use for cotton farmers.

**How did you avoid being locked into a single vendor?**
The OAN DPG layer, Beckn protocol, and federated data architecture are the same vendor-independence mechanisms as in MahaVistaar. Specific additional vendor-independence measures at the national level are not documented.

**Were there sovereign or policy guidelines that shaped your technology choices — around data residency, permitted vendors, or infrastructure?**
Not documented.

**Did any data source or system integration turn out to be harder than expected?**
Not documented. The deployment was newly launched at the time of source documentation.

**Did the AI ever give a wrong or harmful answer to a user — and how did you catch and handle it?**
Not documented.

**What did you put in place to prevent the AI from causing harm — and was it ever tested?**
The OAN architecture includes the independent moderation layer (GPT-OSS Safeguard 20B in the MahaVistaar implementation) as a shared architectural component. Whether and how this is implemented at the national layer specifically is not documented.

---

## C — Institution

*Who deploys AI.*

**How did you get the deployment approved and funded — and did you position it as a one-time project or a long-term transformation initiative?**
Bharat-VISTAAR was announced in the Union Budget 2026-27 in early February 2026 with an allocation of Rs. 150 crore, formally launched by Agriculture Minister Shivraj Singh Chouhan in Jaipur on 17 February 2026, and championed by Prime Minister Modi at the India AI Impact Summit. The Union Budget announcement and PM-level endorsement indicate positioning as a long-term national infrastructure commitment, not a pilot project. The Ministry of Agriculture and Farmers Welfare is the deploying institution.

**Was there internal resistance — and if so, what actually changed minds?**
Not documented.

**Did you need multiple departments or agencies to cooperate — and where did that get difficult?**
The national layer requires state governments to connect their platforms (MahaVistaar, Bihar Krishi) as nodes, and requires ICAR, IMD, and PM scheme databases to expose their data through the national integration layer. The OAN source document records that state-level onboarding was ongoing at the time of launch. Specific inter-institutional friction points are not documented.

**Did procurement rules create a barrier — and if so how did you get through them?**
Not documented.

**When something went wrong, who was accountable — and was that clear from the start?**
Not documented.

**What happens to this deployment if the key person driving it moves to a different role?**
Not documented.

**Was there a leadership or political change during the deployment, and how did it affect things?**
Not documented.

### Additional Insights

The Ministry of Agriculture and Farmers Welfare's role — as documented in OAN source material — is as "national integrator," not as a platform builder replacing state systems. The OAN source document states explicitly: "Bharat-VISTAAR does not replace what Maharashtra, Gujarat, or Bihar have built. It amplifies them." For a national government considering this pathway, the implication is that the institutional design question is not "how do we build the national platform?" but "how do we create the common rail that makes state-level investments compound rather than duplicate?"

---

## D — Ecosystem

*Who executes.*

**How many organisations had to work together for this to function?**
At Phase 1 launch: ICAR (knowledge corpus), IMD (weather), NPSS (pest alerts), AgriStack (farmer registry), the PM scheme database systems, and the state-level node deployments (MahaVistaar, Bihar Krishi, Amul Sarlaben). Full central scheme integration was targeted for May 2026, implying additional agency integrations ongoing at the time of source documentation.

**Who was ultimately responsible for keeping all of them aligned — and what did that role actually involve?**
Not documented.

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
Not documented at the national layer. State-level workforce impacts are documented in the respective state pathway pages ([MahaVistaar](mahavistaar.md), [Bihar Krishi](bihar-krishi.md)).

**How and when were they brought in, and what did they need to learn?**
Not documented.

**Was there resistance from staff — and if so what worked to address it?**
Not documented.

**How did you train staff at scale — especially those in low-connectivity or low-literacy contexts?**
Not documented.

**After the deployment, could staff still do their job if the system was unavailable — or had they become dependent on it?**
Not documented.

---

## F — Operating Model

*What makes it last.*

**What did this cost to build, and what does it cost to run annually?**
The Union Budget 2026-27 allocation is Rs. 150 crore. How this is divided between build and operation, and over what period, is not documented.

**What did you measure to know it was working — and what did the numbers actually show?**
Phase 1 was live with 10 major central schemes (PM-KISAN, PMFBY, Soil Health Card, Kisan Credit Card) and IMD weather and NPSS pest alerts operational at launch. User volume and engagement metrics are not documented for the national layer separately from its state nodes.

**Who owned operations after the pilot ended, and how was that handover structured?**
Not documented. The deployment had just launched at the time of source documentation.

**Was there an outcome or a problem that showed up later that you wished you had been measuring from the start?**
Not documented.

**Was there a point where the whole thing nearly stalled — and what got it through?**
Not documented.

**Were there compliance, audit, or regulatory requirements that shaped how you ran operations?**
Not documented.

---

## Reusable Toolkit

No reusable assets documented separately from the OAN DPG layer. See [MahaVistaar Reusable Toolkit](mahavistaar.md#reusable-toolkit) for the shared architectural assets.

---

## Related Pathways

- [MahaVistaar](mahavistaar.md) — Anchor OAN deployment; connects to Bharat-VISTAAR as its Maharashtra node
- [Amul Sarlaben](amul-sarlaben.md) — Gujarat cooperative node on the Bharat-VISTAAR national layer
- [Bihar Krishi](bihar-krishi.md) — Bihar state node, built independently and then connected to the national layer
- [Ethiopia ATI](ethiopia-ati.md) — First international OAN deployment; comparable design question for a different national context

## Related Entities

- [EkStep Foundation](../entities/ekstep-foundation.md)
- [OpenAgriNet](../entities/openagri-net.md)

## Lineage

Built on [MahaVistaar](mahavistaar.md) — architecture, governance frameworks, deployment playbooks, and operational learnings from Maharashtra's nine-month founding deployment provided the foundation for the national layer.
