# Bihar Krishi — Pathway

**Deployment:** Bihar Krishi Agricultural Advisory Platform
**Contributor:** Government of Bihar / MicroSave Consulting / Gates Foundation
**Sector:** Agriculture
**Geography:** Bihar, India (all 38 districts)
**Actor type:** Government
**Journey stage:** Scaling
**Dimensions covered:** A, C, D, E, F
**Horizontal or vertical:** Vertical (sector-specific)
**Deployment status:** Active
**Last updated:** 2026-06-02
**Contact for peer connection:** Government of Bihar / MicroSave Consulting

## Summary

Bihar Krishi is a state government agricultural platform built under Bihar's 4th Agriculture Roadmap, designed and delivered with MicroSave Consulting and Gates Foundation support to address one of India's most severe agricultural advisory gaps: historically barely one agriculture field officer for every 2,000 farmers. It unified 50+ fragmented state agricultural services, trained 15,000+ extension workers, registered 850,000+ farmers across all 38 districts, and received the ET DigiTech Award 2025 (Gold) and SKOCH Award 2025 (Gold). Unlike other OAN pathway deployments, Bihar Krishi was built independently — not on the OAN architecture — and later connected to Bharat-VISTAAR as its Bihar node. This pathway is useful to adopters asking how a state government with severe structural constraints can build a coherent agricultural platform from the ground up, and how an independently-built deployment connects to a national layer.

---

## A — Problem Orientation

*What you build on.*

**Who were you trying to serve, and what specific problem were you solving for them?**
Bihar Krishi targets Bihar's farming population, of whom 25% are women. The structural gap was severe: historically barely one agriculture field officer for every 2,000 farmers — making timely, personalised advisory structurally impossible through the human extension system alone. Bihar is a predominantly rural economy with deep exclusion from timely advisory, scheme access, and market information. The platform was designed to address all three simultaneously through a unified digital interface.

**What were the access constraints of your users — language, literacy, connectivity — and how did that shape what you built?**
Not documented in available source material beyond the implication that the platform was designed for a predominantly rural, low-income population with limited prior digital service access.

**Was there data already available to start with, or did you have to build or collect it first?**
Bihar's 4th Agriculture Roadmap provided the strategic framework. The platform unified 50+ government schemes into a coherent access point — implying that scheme data existed in fragmented state systems and the design work was integration rather than creation. Specific data preparation challenges are not documented.

**Why did this problem need AI — what would a non-AI solution have missed?**
Not documented specifically for Bihar Krishi. The structural gap (1 field officer per 2,000 farmers) implies the same hard scaling ceiling as other deployments on this pathway: human advisory capacity cannot reach 850,000+ registered farmers at the frequency decisions require. Digital unification of 50+ schemes suggests that AI-enabled natural language access may reduce the navigational burden on farmers seeking scheme eligibility, but whether the deployed system uses AI inference at the same level as MahaVistaar is not documented.

**Did users interact through voice, an app, or something else — and what drove that choice?**
Not documented in available source material.

**Did your understanding of the problem change after you started — and if so, how?**
Not documented.

**Is there anything about your users you assumed early on that turned out to be wrong?**
Not documented.

---

## B — Architecture

*What you build with.*

**Did you bring data together into one place or connect to it where it lived — and why?**
The platform unified 50+ state government schemes into a coherent access point. Whether it adopted a federated data connection approach or a centralised data model is not documented in available source material.

**How did you keep data from multiple sources current and consistent in production?**
Not documented.

**What did you build yourself versus use something that already existed?**
Bihar Krishi was described in the OAN source document as "a rigorous, ground-up effort to unify fragmented state agricultural services into a coherent platform." It was not built on OAN architecture — it was built independently under Bihar's 4th Agriculture Roadmap. When Bharat-VISTAAR launched, Bihar Krishi connected to it as the Bihar node, adding access to the national knowledge base, AgriStack, and ICAR data through the national layer.

**How did you avoid being locked into a single vendor?**
Not documented.

**Were there sovereign or policy guidelines that shaped your technology choices — around data residency, permitted vendors, or infrastructure?**
Not documented.

**Did any data source or system integration turn out to be harder than expected?**
Not documented.

**Did the AI ever give a wrong or harmful answer to a user — and how did you catch and handle it?**
Not documented.

**What did you put in place to prevent the AI from causing harm — and was it ever tested?**
Not documented.

---

## C — Institution

*Who deploys AI.*

**How did you get the deployment approved and funded — and did you position it as a one-time project or a long-term transformation initiative?**
Bihar Krishi was designed within Bihar's 4th Agriculture Roadmap — a state-level strategic framework — providing formal institutional anchoring. Gates Foundation provided funding support. MicroSave Consulting provided implementation support. The roadmap framing indicates a long-term transformation intent. Specific budget amounts and internal approval mechanisms are not documented.

**Was there internal resistance — and if so, what actually changed minds?**
Not documented.

**Did you need multiple departments or agencies to cooperate — and where did that get difficult?**
Unifying 50+ government schemes into a coherent platform implies significant cross-departmental cooperation. Specific inter-departmental friction points are not documented.

**Did procurement rules create a barrier — and if so how did you get through them?**
Not documented.

**When something went wrong, who was accountable — and was that clear from the start?**
Not documented.

**What happens to this deployment if the key person driving it moves to a different role?**
Not documented.

**Was there a leadership or political change during the deployment, and how did it affect things?**
Not documented.

### Additional Insights

Bihar Krishi represents a distinct path through the same structural problem that OAN deployments address: Bihar built on its own terms first, established proof, then connected to the national layer. The OAN source document frames this as "a state that built first on its own terms, then connected. Bihar Krishi was a rigorous, ground-up effort to unify fragmented state agricultural services into a coherent platform." For a next adopter in a state context where the national OAN architecture is not yet established, this demonstrates that ground-up state platform development is viable — and that an independently-built platform can subsequently become a node in a national architecture without requiring a rebuild.

---

## D — Ecosystem

*Who executes.*

**How many organisations had to work together for this to function?**
Government of Bihar as deploying institution; MicroSave Consulting as implementation partner; Gates Foundation as funder; state agricultural scheme-owning departments (50+ schemes implies 50+ data contributors or aggregated scheme systems). Exact ecosystem scope is not documented.

**Who was ultimately responsible for keeping all of them aligned — and what did that role actually involve?**
Government of Bihar, with MicroSave Consulting as the implementation coordination partner. Specific role definition is not documented.

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
Yes — 15,000+ extension workers were trained as part of the deployment. This is the largest documented workforce training number in the OAN source material and indicates that extension worker enablement was a core component of the Bihar deployment, not an afterthought.

**How and when were they brought in, and what did they need to learn?**
Not documented beyond the 15,000+ trained figure.

**Was there resistance from staff — and if so what worked to address it?**
Not documented.

**How did you train staff at scale — especially those in low-connectivity or low-literacy contexts?**
Not documented. The scale (15,000+ extension workers across 38 districts) implies a structured multi-site training programme, but the methodology is not documented in available source material.

**After the deployment, could staff still do their job if the system was unavailable — or had they become dependent on it?**
Not documented.

### Additional Insights

Bihar's 15,000+ extension worker training figure is significant in a cross-deployment context. MahaVistaar's "training = use" design for farmers deliberately avoided a training bottleneck; Bihar Krishi's documented investment in training 15,000+ extension workers suggests that the extension workforce was treated as a critical adoption vector rather than a passive recipient of the technology. Whether this reflects a different adoption strategy or a different technology model (e.g., extension-officer-mediated rather than farmer-direct access) is not documented, but the contrast is worth flagging for a next adopter deciding how to engage the extension workforce.

---

## F — Operating Model

*What makes it last.*

**What did this cost to build, and what does it cost to run annually?**
Not documented. Gates Foundation funding support is named but amounts are not documented.

**What did you measure to know it was working — and what did the numbers actually show?**
Since May 2025: 850,000+ farmers registered; coverage across all 38 districts; 38,000+ scheme applications submitted; 20–25% monthly engagement rate; 20 million farmers reached through digital outreach. Awards received: ET DigiTech Award 2025 (Gold) and SKOCH Award 2025 (Gold). Whether the 20% monthly engagement rate is calculated against the 850,000 registered base or a different denominator is not specified.

**Who owned operations after the pilot ended, and how was that handover structured?**
Not documented. Government of Bihar is the institutional owner.

**Was there an outcome or a problem that showed up later that you wished you had been measuring from the start?**
Not documented.

**Was there a point where the whole thing nearly stalled — and what got it through?**
Not documented.

**Were there compliance, audit, or regulatory requirements that shaped how you ran operations?**
Not documented.

---

## Reusable Toolkit

No reusable assets documented in available source material.

---

## Related Pathways

- [MahaVistaar](mahavistaar.md) — Pioneer OAN deployment; architecture and learnings now accessible to Bihar through Bharat-VISTAAR connection
- [Bharat-VISTAAR](bharat-vistaar.md) — National layer that Bihar Krishi connected to, gaining access to AgriStack, ICAR data, and PM schemes
- [Amul Sarlaben](amul-sarlaben.md) — Cooperative context comparison; very different institutional starting point, similar structural exclusion problem

## Related Entities

- [EkStep Foundation](../entities/ekstep-foundation.md)
- [OpenAgriNet](../entities/openagri-net.md)

## Lineage

Bihar Krishi was built independently under Bihar's 4th Agriculture Roadmap — not as an OAN deployment. Connection to [Bharat-VISTAAR](bharat-vistaar.md) subsequently gave it access to national knowledge resources. OAN amplified what Bihar had already built; it did not originate it.
