# Blue Dots — Pathway

**Deployment:** Blue Dots District Livelihoods Employment Discovery
**Contributor:** EkStep Foundation
**Sector:** Livelihoods
**Geography:** Ghaziabad (Uttar Pradesh) and Dharwad (Karnataka), India — pilot districts; playbook designed for replication
**Actor type:** Government
**Journey stage:** Scaling
**Dimensions covered:** A, C, D, E, F
**Horizontal or vertical:** Vertical (sector-specific)
**Deployment status:** Active
**Last updated:** 2026-06-02
**Contact for peer connection:** EkStep Foundation

## Summary

The Blue Dots approach converts a district's employment landscape from invisible to live: youth, women, and employers become discoverable "Blue Dots" on a digital map, enabling continuous daily matching rather than episodic job fairs. Piloted in Ghaziabad (UP) and Dharwad (Karnataka), it reduced employer hiring costs approximately 10× and cut time-to-fill from weeks to days or hours. The approach is primarily a digital discovery and coordination infrastructure, not an AI inference system — its value is in making labour markets legible rather than in AI-generated recommendations. This pathway is useful to adopters asking how a district government can build a functioning local employment exchange from existing institutional data, and how to create a self-sustaining ecosystem of local actors around a credible discovery infrastructure.

---

## A — Problem Orientation

*What you build on.*

**Who were you trying to serve, and what specific problem were you solving for them?**
The deployment serves youth, women, and local employers within a district. Employment discovery in India's local labour markets is "digitally dark" — people and employers are geographically nearby but invisible to each other. Lists of job seekers sit in registers and spreadsheets; job openings circulate through word of mouth; trust breaks down when information cannot be verified. Both employers and talent candidates prefer local proximity — but the infrastructure to find each other continuously and at low cost did not exist. The Blue Dots approach makes local labour markets legible on a shared digital map.

**What were the access constraints of your users — language, literacy, connectivity — and how did that shape what you built?**
Not documented in detail. The approach uses consent-based digital profiles — youth and employers confirm their visibility before appearing on the map — implying basic mobile phone access. Data collection uses simple formats: for youth, name, contact, skills, location, and willingness for local jobs; for employers, role, openings, location, and salary. Simplicity of the data model reflects that the target population may not have consistent digital access or literacy.

**Was there data already available to start with, or did you have to build or collect it first?**
Existing institutional data — alumni records from ITIs, job fair data, Udyam registration records, college placement data, local government scheme registries — is the primary source for initial Blue Dot creation. The approach explicitly instructs districts to "unlock government and institutional databases" rather than collecting data from scratch. Bulk onboarding from ITIs, colleges, MSME associations, NGOs, and skilling centres populates the map within 2–4 weeks.

**Why did this problem need AI — what would a non-AI solution have missed?**
The Blue Dots approach is primarily a digital mapping and discovery infrastructure rather than an AI inference system. The core intervention is making existing data legible, searchable, and continuously updated on a shared platform — not AI-generated matching or recommendation. Whether AI matching algorithms underpin the platform is not documented. What the approach provides that a purely analogue system cannot: continuous discovery (not episodic), instant geographic filtering, verified profile credibility, and digital shortlisting speed. The 10× cost reduction in employer hiring and reduction from weeks to days/hours reflects the value of digitising discovery, not AI inference specifically.

**Did users interact through voice, an app, or something else — and what drove that choice?**
The platform delivers a digital map view to district teams, employers, and job seekers. The DigiPass (a verified digital token issued to shortlisted candidates) functions as a digital credential usable across multiple interviews. Whether there is a mobile app, web interface, or WhatsApp channel is not specified in the source playbook. Employer shortlisting and youth matching are described as continuous processes mediated through the platform.

**Did your understanding of the problem change after you started — and if so, how?**
Not documented.

**Is there anything about your users you assumed early on that turned out to be wrong?**
Not documented.

### Additional Insights

The Ghaziabad and Dharwad pilots revealed that proximity is a meaningful signal on both sides of the labour market: employers discovered local talent they did not know existed, and youth could see jobs nearby that they could not previously find. The playbook records this as a non-obvious finding: the constraint was not geographic distance but digital invisibility. Once the map existed, proximity surfaced as a strong matching factor on its own. For a next adopter, this suggests that simply making the labour market visible — before any active matching or recommendation — may produce faster hiring outcomes than anticipated.

---

## B — Architecture

*What you build with.*

**Did you bring data together into one place or connect to it where it lived — and why?**
Data is collected and consolidated into a district-level platform: youth profiles, employer listings, and institutional data (ITIs, colleges, MSME associations) are bulk-uploaded and maintained in a shared system that powers the digital map. Unlike the OAN agricultural deployments, the Blue Dots approach centralises discovery data rather than federating it — because the value of the platform depends on a single searchable, mappable data layer visible to all ecosystem actors simultaneously.

**How did you keep data from multiple sources current and consistent in production?**
Weekly nudges to youth and employers ("Still looking for work?", "Still looking to hire?") update profile status. Bulk uploads from institutional sources (ITIs, colleges) refresh the pool. The Jobs Facilitation Centre (JFC) coordinates ongoing data quality and updates. Monthly reviews track outcomes and identify stale or unverified data.

**What did you build yourself versus use something that already existed?**
The playbook describes a platform that the EkStep Foundation seeded — but the specific technology stack (whether open-source, proprietary, or built on existing government systems) is not documented. The DigiPass credential and the digital map visualisation are named as distinct platform components. Local innovators are invited to build tools for "bulk uploads, vernacular resumes, or map visualisation" on top of the platform — implying an open or accessible data layer.

**How did you avoid being locked into a single vendor?**
Not documented.

**Were there sovereign or policy guidelines that shaped your technology choices — around data residency, permitted vendors, or infrastructure?**
Not documented.

**Did any data source or system integration turn out to be harder than expected?**
Not documented.

**Did the AI ever give a wrong or harmful answer to a user — and how did you catch and handle it?**
Not applicable — the platform is primarily a discovery and mapping infrastructure, not an AI inference system delivering advisory responses.

**What did you put in place to prevent the AI from causing harm — and was it ever tested?**
Not applicable in the same sense as AI advisory deployments. The consent mechanism — only profiles confirmed with "YES" by the individual appear on the map — provides a form of user-controlled data governance. "Strict monitoring and accountability" for irregularities is referenced in the Project Astitva booklet in the same source package, but not specifically for Blue Dots.

---

## C — Institution

*Who deploys AI.*

**How did you get the deployment approved and funded — and did you position it as a one-time project or a long-term transformation initiative?**
The Blue Dots playbook positions the approach as a permanent transformation of the district's employment infrastructure — continuous discovery, not episodic job fairs — rather than a project with an end date. The playbook explicitly requires "a single government champion (DC / Mission Director / Secretary level) who owns outcomes, not just approvals" before any on-ground action begins. EkStep Foundation seeded the approach. Government funding for the district-level PMU and JFC is implied by the government-led framing, but specific budget amounts are not documented.

**Was there internal resistance — and if so, what actually changed minds?**
Not documented.

**Did you need multiple departments or agencies to cooperate — and where did that get difficult?**
Step 0 of the playbook requires aligning relevant state-level authorities: skilling-related departments, labour and employment departments, and MSME/industry departments. At the district level, the Jobs Facilitation Centre (JFC) brings the district administration, employment exchange, skills office, and MSME associations together. The playbook identifies inter-departmental alignment as a prerequisite, not an afterthought — reflecting that data sits across these agencies and access requires formal alignment.

**Did procurement rules create a barrier — and if so how did you get through them?**
Not documented.

**When something went wrong, who was accountable — and was that clear from the start?**
Not documented.

**What happens to this deployment if the key person driving it moves to a different role?**
Not documented. The playbook's emphasis on the JFC as an institutional structure — rather than a person — provides some continuity design, but key-person dependency is not explicitly addressed.

**Was there a leadership or political change during the deployment, and how did it affect things?**
Not documented.

### Additional Insights

The playbook's Step 0 — "Align Outcomes, Context and Ownership before initiating any on-ground action" — directly mirrors the OAN pathway's institutional sequencing lesson from MahaVistaar: identify and secure a named government champion before any technology choices. The Blue Dots playbook makes this explicit: the champion must own outcomes, not just approvals. For a next adopter, the distinction matters — an official who approves the initiative but does not own outcomes will not unblock the inter-departmental data-sharing that makes the map possible.

---

## D — Ecosystem

*Who executes.*

**How many organisations had to work together for this to function?**
The Jobs Facilitation Centre (JFC) is a 6–8 member institutional structure that brings together representatives from government offices (employment exchange, DC office, skills office, MSME associations), not-for-profits (local NGOs connected to youth and employers), and local industry players. The playbook identifies five categories of ecosystem actor: government departments (creating youth Blue Dots), employer-side departments (creating job Blue Dots), local ecosystem actors who leverage the discovery infrastructure (coaching centres, staffing firms, assessment firms, interview prep firms, counselling firms), local innovators who extend the platform, and the JFC itself as coordinator. The total number of organisations active in Ghaziabad and Dharwad is not specified.

**Who was ultimately responsible for keeping all of them aligned — and what did that role actually involve?**
The District Collector (DC) or equivalent government lead chairs monthly JFC reviews and owns the rhythm. The 2–3 member district PMU handles day-to-day coordination: putting together the district pilot plan, coordinating with ecosystem partners, facilitating progress, and convening regular check-ins. The JFC as an institution is the alignment mechanism — monthly reviews, quarterly employment bulletins, daily blue dot creation — rather than a single named individual.

**Were there situations where partners had competing mandates or priorities — and how were those resolved?**
Not documented.

**Did any partner relationship not work out as expected — what happened and how did you handle it?**
Not documented.

**How was trust maintained across partners — especially when something went wrong?**
Not documented.

### Additional Insights

The playbook's ecosystem design deliberately gives local innovators — coaching centres, staffing firms, assessment firms, third-party aggregators, YouTubers — direct access to the discovery infrastructure. The explicit reasoning is that these actors "stop spending time on mobilising people and businesses and instead focus on outcomes." By sharing the discovery infrastructure with the local commercial ecosystem, the platform makes itself useful to actors with financial incentive to sustain usage. This is a self-reinforcing design: discovery infrastructure that commercial actors depend on gets maintained even when government attention shifts.

---

## E — Workforce

*Who absorbs AI.*

**Were there people — field workers, extension officers, call centre staff — whose job changed because of this deployment?**
The JFC's 6–8 members are the core operational workforce: their role is to run the daily-weekly-monthly rhythm of blue dot creation, nudging, ecosystem engagement, and review. The employment exchange, which previously mediated job fairs and placement drives, shifts toward continuous data coordination and ecosystem activation rather than episodic events.

**How and when were they brought in, and what did they need to learn?**
The JFC is formed in Step 1 before any blue dots are created — institutional formation precedes data collection. The playbook's Step 2 begins with bulk onboarding of data, implying that JFC members learn the platform by using it to onboard institutional data from ITIs, colleges, and MSME associations. Whether formal training on the platform is provided before this is not documented.

**Was there resistance from staff — and if so what worked to address it?**
Not documented.

**How did you train staff at scale — especially those in low-connectivity or low-literacy contexts?**
Not documented. The workforce in this deployment (district government officials, JFC members) is presumed to have basic digital access, unlike the end users (youth, women, employers) who may not.

**After the deployment, could staff still do their job if the system was unavailable — or had they become dependent on it?**
Not documented. However, the playbook's emphasis on "simple routines" as the foundation of success — rather than technology — suggests that the approach is designed to be operationally resilient: the rhythm (daily nudges, weekly reviews, monthly meetings) continues even if specific platform features are unavailable.

---

## F — Operating Model

*What makes it last.*

**What did this cost to build, and what does it cost to run annually?**
Not documented. The district PMU (2–3 members) and JFC (6–8 members) represent the primary staffing cost. Technology costs are not documented.

**What did you measure to know it was working — and what did the numbers actually show?**
Before Blue Dots in Ghaziabad and Dharwad: employers spent ₹1,000 per hire; weeks to fill vacancies; one-off job fairs; unverified candidates. After: hiring costs dropped approximately 10×; roles filled within days or hours; continuous daily shortlists and interviews; credible verified profiles. The playbook frames success as "when discovery becomes routine, hiring becomes reliable" — predictability and continuity, not volume of placements, as the primary success indicator. Specific placement volumes from Ghaziabad and Dharwad are not documented.

**Who owned operations after the pilot ended, and how was that handover structured?**
The JFC as an institutional structure is designed to own ongoing operations — not EkStep Foundation and not a specific government individual. The monthly JFC review, chaired by the DC, and the quarterly District Employment Bulletin are the governance rhythm that sustains ownership. Whether a formal handover from EkStep to the district occurred, and how it was structured, is not documented.

**Was there an outcome or a problem that showed up later that you wished you had been measuring from the start?**
Not documented.

**Was there a point where the whole thing nearly stalled — and what got it through?**
Not documented.

**Were there compliance, audit, or regulatory requirements that shaped how you ran operations?**
Consent mechanism: only profiles confirmed by the individual with "YES" appear on the district map. This is a data governance mechanism — not a formal regulatory requirement — but it is positioned as foundational to the platform's credibility.

### Additional Insights

The playbook explicitly states: "The Ghaziabad & Dharwad experience showed that success can be enabled by technology, but thrives on simple routines, and a local district ecosystem organising itself around the initiative." This is a direct statement that the technology is not the primary factor in whether the approach works. The daily-weekly-monthly rhythm (daily: create blue dots; weekly: nudges and ecosystem engagement; monthly: JFC review; quarterly: employment bulletin) is the operational design that sustains the platform. For a next adopter, investing in the rhythm is as important as investing in the platform itself — and the playbook is explicit that a rhythm that pulses like a heartbeat is what makes discovery reliable rather than sporadic.

---

## Reusable Toolkit

| Asset | Type | What it is useful for | How to access |
|---|---|---|---|
| Blue Dots playbook | Implementation guide | Step-by-step district setup: PMU formation, JFC establishment, data onboarding, daily-weekly-monthly rhythm, local ecosystem activation | Via EkStep Foundation |
| DigiPass | Digital credential | Verified token for shortlisted candidates, reusable across multiple interviews; reduces employer screening uncertainty | Via EkStep Foundation / district platform |
| JFC structure template | Governance model | 6–8 member institutional structure for continuous employment discovery; reusable across districts | Documented in Blue Dots playbook |
| Communication timing guide | Operational template | Who to engage, when, and what to communicate from Day 1 through ongoing activation | Documented in Blue Dots playbook |

---

## Related Pathways

No other livelihoods pathway pages currently documented. See [Agriculture sector](../sectors/agriculture.md) for comparable deployments in a different sector using the same EkStep Foundation ecosystem.

## Related Entities

- [EkStep Foundation](../entities/ekstep-foundation.md)

## Lineage

Not documented. The Blue Dots approach was seeded by EkStep Foundation; no prior pathway is identified as the lineage source.
