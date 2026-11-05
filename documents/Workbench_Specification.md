# Case Management Workbench: pre-build specification

Version 1.0 for review. Prepared 6 November 2026. No MVP code, site or integrations have been built. Product behavior below is a proposed specification, not a clinically validated system. The visual direction remains pending user review.

## 1. Brief alignment and delivery map

The HiLabs brief requests an 8-12 slide deck or equivalent PDF and a spreadsheet annex. The accompanying 12-slide review deck covers A-E. The annex contains five original fictional patients with records across 13 patient-linked datasets, planted imperfections and Monday action lines. This specification expands behavior and acceptance criteria for the later build. Design_References.md contains ten researched references and three visual directions.

| Brief part | Coverage |
|---|---|
| A. Understand | Slides 1-2; sections 2-3; problem ranking and time assumptions |
| B. Data strategy | Slides 3-4; annex Data strategy; section 5 |
| C. Synthetic patients | Slides 5-6; annex Monday actions and source tables; section 6 |
| D. Product design | Slides 7-10; three wireframes, hierarchy, next-action rules, AI confirmation and three walkthroughs |
| E. Prioritize and measure | Slide 11; sections 8-10 |
| Optional pilot and GTM | Slide 12; section 11 |

The brief's example patient is not reused. We follow its explicit stable unique member-ID assumption. Imperfections affect event duplication, source content, recency and contact accuracy, not member identity.

## 2. User and problem

Primary persona: Demo Maria, RN case manager at a health plan. Twenty years of ICU experience and 48 active cases are assignment scenario inputs. She coordinates and coaches by phone, reviews records, arranges services, checks outcomes and documents. She does not prescribe through this workbench. Social-work and behavioral-health case managers use the same core workflow, with appropriate permissions. Patients and buyers are not additional app personas in this submission.

Goal: at 8 am, understand whom to work on, what changed, which evidence is reliable, and the next useful action. During contact, reuse confirmed facts and capture a patient-agreed plan. Afterwards, verify whether care happened.

Current day: review alerts and lists, reconstruct patient context across systems, attempt contact, assess needs, coordinate external services, document, and return to unresolved cases. Missed calls and external waiting create repeated loops rather than a linear one-visit process.

### Illustrative day model, not measured research

One 480-minute shift = 120 documentation + 90 information search/reconciliation + 60 unsuccessful outreach + 60 coordination + 90 patient/caregiver conversations + 60 breaks, huddles and other duties. Total 480. Potential avoidable friction is a subset of each category, not every minute of administration.

Pilot hypothesis: save 30 documentation + 30 preparation + 15 failed-outreach minutes = 75 minutes/day. Baseline conversations are 90 minutes; full reinvestment could yield 165, but this is a capacity hypothesis, not a promised outcome. Measure time in mutually exclusive categories over two baseline weeks. Sample different case types and record uncertainty. Do not generalize one plan's experience nationally.

## 3. Problems and prioritization

P = patient impact (35%), T = time burden (25%), R = reach across routine work (20%), A = MVP addressability (20%). All 1-10. Weighted score is a judgment informed by research, not a measured effect. Scores within 0.3 should be considered ties. Avoid double-counting dependent problems when discussing total benefit.

| Problem | P | T | R | A | Score |
|---|---:|---:|---:|---:|---:|
| Fragmented/untrustworthy patient picture |10|9|10|9|9.55|
| Unclear daily priorities and next actions |10|8|9|8|8.90|
| Duplicate documentation |7|10|10|9|8.75|
| Lost tasks, referrals and handoffs |9|8|9|9|8.75|
| Ineffective outreach |9|8|9|8|8.55|
| Medication uncertainty |10|7|8|7|8.25|
| Missing social, behavioral, caregiver context |9|7|8|7|7.85|
| Caseload overload and poor allocation |9|8|8|5|7.75|
| Unclear team ownership |8|8|8|6|7.60|
| Coverage/authorization barriers |9|8|7|4|7.35|
| Low trust and mismatched patient goals |9|7|8|4|7.25|
| Alert overload |8|7|7|6|7.15|
| Cost-proxy risk bias |10|4|7|5|6.85|
| Unavailable external services |10|7|7|1|6.85|
| Consent/access uncertainty |8|6|7|5|6.65|
| Poor closure/transfer |8|5|6|7|6.65|
| Activity-only measurement |7|5|8|6|6.50|
| Usability/training/downtime |6|7|6|6|6.25|

Evidence map: S2 supports information access, duplication and consent uncertainty; S4 illustrates prioritization and operational work; S5 supports medication reconciliation; S6 supports engagement/access barriers; S7 supports referral fragmentation; S8 supports external service limits; S10-S12 support bias, alert and authorization risks. Team allocation, closure, measurement and the exact daily-priority experience remain discovery hypotheses for this plan.

The first five form the MVP. Medication and social needs appear inside the summary and tasks from day one. Advanced medication decision support and service-capacity management remain later work.

## 4. Workflow and state model

| Stage | Case-manager action | Workbench support | Exit condition |
|---|---|---|---|
| Identify and assign | Review trigger, check fit and ownership | Source-linked trigger, program, eligibility, duplicate-case warning | Assigned named owner or reasoned screen-out |
| Prioritize | Review deadline, change and existing plan | Explained tier, due date, filters, override | Next case and action chosen |
| Prepare | Review record, medication conflicts, contact route | Member summary, timeline, source drawer | Questions and missing facts identified |
| Outreach | Check permissions, call patient/caregiver | Preferred time/language, valid route, attempt history | Reached, declined, no answer or invalid route recorded |
| Assess and agree | Ask about real needs and member goals | Prefilled known facts with editable unknowns | Patient-agreed goals and barriers recorded |
| Coordinate | Contact providers/services and assign follow-ups | Owner, due date, service, dependency and status | Action assigned; external response pending or received |
| Monitor | Verify attendance, medicine access or service start | Due tasks, evidence capture and reminders | Verified outcome or renewed follow-up |
| Document | Review note and plan, sign | Reusable facts and draft assistance | Signed note; audit event; amendments versioned |
| Close/transfer | Review goals and unresolved items | Closure checklist, reason, receiving owner | Outcome recorded and transfer accepted if applicable |

Case states: New, Review, Outreach, Active, Monitoring, Closed. Outreach failures are contact outcomes, not case closure. Reopen requires reason and owner. Declined participation can close with reason and appropriate handoff under plan policy. Screen-out differs from successful completion. Unable-to-reach closure needs the plan's approved attempt policy and clinician review; the app does not invent an attempt-count rule.

Task states: Open, In progress, Waiting external, Completed, Cancelled. Referral detail additionally tracks Requested, Accepted, Service received, Verified, Unavailable and Declined. Waiting external still has an internal owner and review date. Completion requires evidence type/date/source. Cancel requires reason. Overdue is calculated from due time and state.

Contact outcomes: Reached patient, Reached authorized caregiver, No answer, Voicemail, Disconnected, Wrong person, Declined, Rescheduled. Invalid routes stop further suggestions to that number. Preferences do not establish legal consent. Review caregiver scope and expiry before disclosure.

## 5. Data model and trust

Member ID is stable across datasets. Member has many cases. Case has many goals, tasks, referrals, contacts, notes and assessment versions. Clinical events and prescriptions/dispenses attach to the member and can support several cases. An alert must reference the case to which the action belongs; patient-level facts do not automatically complete every case.

Every source observation has record_id, member_id, dataset, source, event/observed_at, received_at, source_as_of, availability status and original content. Every derived insight has supporting record IDs, rule/version, generated_at, limitations and review state. Every edit records actor/time and before/after or version reference. Missing, stale, conflicting and explicitly negative are separate states.

The annex Data strategy lists 18 dataset groups with source, useful fields, desired freshness, quality handling and must/later priority. Existing risk signals can help case finding, but the MVP does not train a new model. A curated service directory and manual external verification support the first pilot. Authorization integration and device monitoring follow later.

### Dataset combinations and decision rules

1. Discharge alert + discharge medication list + pharmacy fills + appointment status: review transition needs, verify medication access and follow-up. Missing fill is a possible gap only, especially if feed coverage is incomplete.
2. Diabetes clinical record/lab + observed fill history + cost assessment + work preference: ask about actual supply/affordability at a suitable time and coordinate support. Do not infer nonadherence or change treatment.
3. Repeated ED events + failed attempts + invalid number + language: change contact strategy, request permitted help from existing care team, refresh contact/social assessment.
4. Patient-reported housing need + referral status + upcoming visit + transport need: verify receipt and availability, arrange feasible follow-up, record unmet need if no service exists.
5. Discharge + caregiver authorization/strain + home-health referral + medication conflict: call authorized caregiver at agreed time, verify service start, route discrepancy to treating team.

Freshness displays event date, received date and feed-as-of. A delivery timestamp is not proof of a current fact. Clinical summary always lists known missing sources. Clinical conflicts persist until an authorized reviewer resolves them; the app preserves alternatives and history. An AI summary cannot silently select a dose.

### Queue policy (proposed operational policy, requires plan approval)

P0 is clinician-confirmed urgent review under the plan's escalation protocol and always sits above routine work. No synthetic patient has a confirmed current emergency. The application must not imply continuous emergency monitoring.

P1: uncontacted discharge within seven calendar days; a clinician-flagged medication conflict or failed essential service start; an overdue high-priority agreed action; or recent ED event with unresolved outreach. P2: possible refill/access gap, unresolved nonurgent barrier or routine follow-up due. P3: monitoring with no current due action. Seven days is a pilot worklist choice, not a clinical guideline. All thresholds and holiday calendars are configurable under governance.

Sort by tier, overdue duration, due time, then event recency. Display all reasons rather than a mysterious numeric risk score. Respect preferred contact time: urgency tier and best contact time are separate. A manager can prepare a high-priority late-afternoon call in the morning. Clinician override requires reason and expiry. Missing data is a verification task, never a low-risk default. Do not use cost alone or ease of contact as priority proxies. Review coverage and fairness across language and contact-access groups.

Pilot transition tasks default to first outreach within two business days after discharge and a follow-up-verification task within seven calendar days, explicitly configurable local assumptions inspired by the brief. CMS TCM billing windows apply to eligible provider services and must not be mislabeled as universal payer obligations [S9]. For a Nov 6 Friday discharge, Monday Nov 9 is business day one if no applicable holiday.

## 6. Synthetic patients and walkthroughs

Demo clock: Monday 9 November 2026, 08:00 America/New_York (UTC-05). This is a fictional demonstration clock, separate from the document's preparation date. All names, providers, plans and records are invented. Phones use fictional 555-01xx numbers and email uses example.invalid. No real addresses or identifiers are included.

### SYN-001: Demo Avery Vale

Fresh heart-failure discharge. Age 68, Medicare Advantage. Goal: Recover at home and attend follow-up. Planted imperfections: Conflicting medication dose and duplicate ADT delivery.

Monday action: Review discharge medication conflict, call Avery this morning, verify access to medicines and confirm the Nov 12 visit and transport.

### SYN-002: Demo Jordan Reed

Diabetes with possible refill gap. Age 54, Commercial PPO. Goal: Keep care affordable around work shifts. Planted imperfections: Observed fill gap may miss outside-network/cash fills; old note says adherent.

Monday action: Contact after 17:30, confirm actual medication supply and affordability, then coordinate pharmacy and diabetes follow-up.

### SYN-003: Demo Riley Moss

Frequent ED use and failed outreach. Age 39, Medicaid. Goal: Establish reliable follow-up and a contact route. Planted imperfections: Wrong phone; duplicate ADT; stale social assessment; appointment status unavailable.

Monday action: Review Nov 7 ED event and missing discharge details; validate an alternate contact route through the care team and arrange Spanish-language outreach within recorded permissions.

### SYN-004: Demo Morgan Brook

Behavioral health and housing instability. Age 31, Medicaid. Goal: Maintain appointments while finding stable housing. Planted imperfections: Referral marked sent but service not received; March address stale.

Monday action: Call at the agreed time about housing referral overdue since Nov 6; confirm safe contact preferences and behavioral-health follow-up. Track availability rather than claim housing is secured.

### SYN-005: Demo Casey Finch

Caregiver strain after discharge. Age 81, Dual eligible MA/Medicaid. Goal: Remain at home with reliable support. Planted imperfections: Home-health status shows referral accepted but start-of-care unconfirmed; medication status conflict.

Monday action: Contact authorized daughter after 16:00, verify home-health start and transport, and review conflicting medication instructions with the treating team.

Each patient has member, case, ADT availability, clinical record, pharmacy, claim, appointment, contact/consent, outreach, assessment, task/referral and plan/note records. For patients without hospital evidence, ADT is explicitly unavailable rather than an invented admission. The annex does not reuse the brief's COPD example.

Walkthrough A, Avery: queue explains discharge and dose conflict; patient view shows original 20mg clinic and 40mg discharge statements with timestamps; outreach prepares verification questions; clinician creates a treating-team reconciliation task and confirms access/transport with Avery; note stays draft until reviewed. No automatic medication order or conflict resolution.

Walkthrough B, Riley: queue explains recent ED event plus failed outreach; summary shows missing discharge detail and invalid number; outreach suppresses that number, shows Spanish need and permitted alternate-route task; document failed contact without fabricating an assessment; keep clinical work open under plan policy.

Walkthrough C, Morgan: queue explains an overdue housing task; patient view separates referral sent from service received; outreach uses neutral-message preference and agreed time; tasks record housing availability and transport for Nov 10; lack of available housing remains an unmet need rather than a false completion.

## 7. Screens and functional specification

The deck contains three layout wireframes. Their fixed hierarchy applies to all visual directions; skin and workspace flexibility remain review choices.

### Screen 1: Daily queue

Above fold: My work, current demo/live date, data-sync state, P1/due/overdue counts, filters, ordered list with member ID, case/program, reason, due time, preferred call time and next action. Click opens the case; secondary action reviews evidence. Filters: assigned to me, program, tier, due date, outreach state and data issue. Search name/member/case ID. Counts reflect filtered context. Do not make four decorative charts the landing page.

### Screen 2: Patient and case view

Pinned identity: name, ID, age, language, case ID/program, owner and state. Above fold: why now, next action, known critical conflicts and source freshness. Main timeline combines dated events. Sections: medications, clinical context, social/caregiver needs, agreed goals, appointments, tasks and source documents. A source drawer shows original statements and audit trail. Conflicting and unknown information cannot disappear inside a polished summary. One member can have more than one case with an explicit case selector.

### Screen 3: Outreach and documentation

Same pinned identity. Left: contact permissions, valid routes, preferred language/time and attempts. Center: structured conversation notes, assessment changes and patient-agreed goals. Right or bottom: draft note, generated tasks and review checklist. Buttons: Log attempt, Save draft, Review and sign. No answer logs a contact outcome without forcing a completed assessment. A signed note can receive an amendment, not silent replacement. Review changed fields before saving updates to the care plan.

### Essential app functions

Role-based sign-in and session handling; assigned work and search; create/assign/transfer/close/reopen case; owner/due/status; task and referral tracking; consent checks; draft persistence and save status; audit trail; notification center; filters; keyboard navigation; empty/loading/error/offline states; manual data correction proposal; reset demo data. Supervisor access serves assignment/escalation, not a new product persona/dashboard in the core case presentation.

For a later synthetic demo, login may use role simulation and all calls/referrals may be simulated. Label these explicitly and never imply real integrations or completed external bookings. A production deployment requires actual identity, tenant separation, access control, secure persistence and integration agreements before real patient data.

### Workspace options

Recommended A: fixed identity and safety strip, reorderable patient tabs, resizable queue/context/notes zones, Focus and Split-note presets, collapse controls and Reset layout. Each tab shows member ID, short name and unsaved state. Patient notifications have a labeled badge distinct from urgency. Tabs can be pinned. Overflow remains searchable. Workspace preferences persist separately from clinical data. Resizing never changes case state.

Cross-patient drag/drop is prohibited. A draft remains bound to original member/case. Switching context never retargets an active draft, task or pending async response. Save failure keeps the draft visibly unsaved and blocks accidental discard. Arbitrary docking, floating windows and cross-patient comparison remain a later optional extension. The design reference file compares A with inbox-first B and chart-first C.

### AI boundaries

Automated with reviewable evidence: event deduplication, age/freshness labels, due-task sorting and deterministic rule explanations. These do not need an LLM.

Optional AI assistance: source-linked summary, note draft from entered notes, extraction suggestions and proposed tasks. It must mark unknowns, preserve conflicts, show supporting records and label drafts. Do not invent numeric confidence. Present evidence as Confirmed, Reported, Inferred, Conflicting or Unknown.

Clinician confirms: assessments, inferred gaps, patient-agreed plan, clinical discrepancy resolution, note signature, outbound messages/referrals and closure. No autonomous prescribing, diagnosis, denial, contact disclosure or case closure. Low-quality/missing sources cause abstention or verification prompts. Provide manual note flow when AI is unavailable. Transcription is later and depends on an approved consent process.

## 8. MVP and later scope

Must: the three screens, source-aware patient record, deterministic queue, structured outreach, reusable documentation, task/referral completion evidence, permission checks, case lifecycle and audit basics. Use standardized upstream data as the brief assumes. A simple curated directory supports coordination. Include all five problems but keep each implementation narrow.

Later: arbitrary panel docking, workload optimization, new predictive models, device streams, full telephony/text delivery, transcription, authorization integration, comprehensive service marketplace, patient portal and automated billing. No pipeline engineering or prescribing platform in this case.

Build sequence after design approval: shared identity/data model and patient view; queue; tasks/referrals; outreach and documentation; optional workspace flexibility; scenario verification. Each stage reuses the same five synthetic patients.

## 9. Metrics and validation

All baselines below are planning assumptions, not researched facts. Replace them with two weeks of baseline measurement. Targets are pilot hypotheses, not commitments. A pilot must not claim causal readmission reduction from a small short sample.

| Metric | Assumed baseline | Pilot target | Definition |
|---|---:|---:|---|
| Median preparation time | 12 min | 7 min | Open case to ready-to-contact, exclude idle time |
| Median documentation time | 10 min | 6 min | Active recording/review time per substantive contact |
| Connect rate | 25% | 35% | Patient/authorized-caregiver reached divided by eligible attempts; stratify by language/contact access |
| On-time high-priority follow-up | 65% | 85% | Eligible due tasks with verified timely completion / all eligible due tasks |
| Referral outcome verified within 7 days | 40% | 60% | Referrals with confirmed status (including unavailable/declined) / referrals due for verification; separately report service received |
| Active caseload | 48 | Hold at 48 initially | Scenario input; protect quality before increasing capacity |
| Wrong-patient save/disclosure | 0 in synthetic review | 0 observed | Any event triggers pause and investigation; small sample cannot prove safety |
| Summary critical-fact error | Unmeasured | 0 observed in reviewed sample | Clinician review of source-to-summary fidelity; report sample size and omissions |

Track clinician overrides, stale-source exposure, alert dismissals, note edits and adoption alongside outcomes. Separate connection from improved health, referral status verification from service delivery, and signed notes from correct notes. Preserve reason codes when excluding records from denominators.

## 10. Risks and mitigations

Wrong/stale data: source dates, missing-feed labels, reviewer confirmation and preserved originals. Medication harm: flag discrepancies and route to treating team, never silently choose or change doses. Alert fatigue: deduplicate, tier and batch routine notifications; acknowledge differs from completion. Automation bias: explain rules and expose evidence/limitations. Equity: avoid cost-only risk ranking, do not deprioritize unreachable members and review outcomes by language/access where appropriate. Privacy: least privilege, scoped caregiver authority, neutral-message preference and audit. Workflow overload: stable defaults, simple navigation and optional flexibility. Service shortages: record unavailable status and escalation rather than inventing resolution. Draft loss/context error: member-bound drafts, explicit save state and concurrent-edit conflict handling.

## 11. Pilot and commercial hypothesis (optional brief bonus)

Buyer: health-plan VP of Care Management, with nursing leadership as clinical sponsor and IT/security/data teams as implementation partners. Start with one transitions/complex-care team of 5-10 managers and roughly 200-400 eligible cases, subject to actual caseload and permissions. Two baseline weeks followed by six pilot weeks. Shadow-mode data/queue review precedes assisted use. Clinicians review all actions.

Measure workflow metrics and source fidelity, plus subgroup gaps. Predefine stop/review conditions for wrong-patient action, inappropriate disclosure or critical misinformation. At pilot end, expand only if preparation/documentation improve without poorer follow-up quality or widening access gaps. Compare matched case types and account for staffing and feed changes. A larger/longer evaluation would be needed for clinical outcome claims.

Pricing signal: test a fixed-fee pilot followed by per-active-case-manager monthly pricing. Illustrative willingness-to-pay probe: $200-$400 per manager/month, explicitly not a market benchmark. At $60/hour loaded labor (assumption), 75 saved minutes/day across 20 workdays represents 25 hours or $1,500/month of gross capacity value; this is not cash savings and excludes software, integration and governance costs. Validate with buyer interviews before pricing. Do not bill by patient contact or imply guaranteed savings.

## 12. Acceptance checklist for the future build

1. All five patients render using one stable member ID across sources; duplicate ADT produces one timeline event with delivery history.
2. Avery's two medication doses remain visible with sources. The manager can create a reconciliation task without changing a prescription.
3. Jordan's missing observed refill reads Possible access/supply gap. Unknown outside-network fills prevent a claim of proven nonadherence.
4. Riley's disconnected number is excluded from suggested calls. Logging failed outreach does not create a completed clinical assessment.
5. Morgan's referral remains unfulfilled until receipt evidence exists; unavailable housing remains an unmet need.
6. Casey's caregiver details are disclosed only within recorded authority. Home-health acceptance differs from service start.
7. Queue explains every tier, respects configured dates, and records clinician overrides. Preferred late contact does not hide clinical priority.
8. Drafts survive tab switching and failed saves with the correct member/case binding. Delayed AI response cannot populate another patient's note.
9. Task completion requires outcome evidence. Case closure reviews unresolved work and records reason/receiving owner.
10. No unanswered field becomes No by default. Empty feeds, delays, conflicts and offline states remain explicit.
11. Every screen has readable labels and keyboard access. Layout reset restores a usable view and patient identity never disappears.
12. Demo actions never send real messages or create external appointments. AI suggestions require human review and a manual fallback.

## 13. Decisions still awaiting user review

Choose visual direction A/B/C and information density after reviewing the ten links. The clinical content, five problems, datasets, synthetic scenarios and functional behavior are proposed in full. Exact visual styling and any optional arbitrary docking remain open. This document does not authorize starting the MVP build.

## Research and source register

- **S1: HiLabs brief.** User-supplied PDF, sections A-E. Assignment requirements; case-manager persona and workload are scenario inputs.
- **S2: Health-plan care-manager information barriers.** https://pmc.ncbi.nlm.nih.gov/articles/PMC6557451/. 80 respondents at one Pennsylvania health plan; published 2017, survey 2012-13. Duplicate entry 68%, multiple logins 49%, timely access 37% rated major barriers. Historical, not national.
- **S3: NCQA case-management framework.** https://www.ncqa.org/programs/health-plans/case-management-cm/. Assessment, planning, coordination, evaluation and advocacy across medical, behavioral and social needs.
- **S4: SummaCare operating policy.** https://www.summacare.com/-/media/project/summacare/website/document-library/medicare-members/medical-benefits/policies/2024---final/complex-care-management-program-documentation-and-outreach.pdf?hash=5010D81309245169D3BCBAEBBE093F7D&sc_lang=en. One plan example of case finding, record review, outreach and documentation; not a universal requirement.
- **S5: Medication reconciliation.** https://digital.ahrq.gov/medication-reconciliation. Information transfer, reconciliation provenance and accountability problems.
- **S6: Patient perspectives.** https://pubmed.ncbi.nlm.nih.gov/35477772/. 2022 qualitative study, 40 patients at 12 primary-care practices. Financial/transport barriers and relationship factors; adjacent setting.
- **S7: Referral tracking research.** https://link.springer.com/article/10.1007/s11606-026-10735-6. 2026 formative community-health-center study; fragmented referral documentation. Adjacent setting.
- **S8: CMS navigation evaluation.** https://www.cms.gov/priorities/innovation/data-and-reports/2026/ahc-final-report. Community service capacity can constrain navigation. Evaluation does not establish this app's impact.
- **S9: CMS transitional care services.** https://www.cms.gov/medicare/payment/fee-schedules/physician-fee-schedule/care-management/transitional-care-management-services. Provider TCM billing has specific contact/visit windows. Do not apply these as universal payer case-management rules.
- **S10: Risk algorithm bias.** https://pubmed.ncbi.nlm.nih.gov/31649194/. 2019 study: cost used as a proxy for need can create racial bias.
- **S11: Alert fatigue.** https://psnet.ahrq.gov/primer/alert-fatigue. Primarily clinical decision-support evidence; apply cautiously to payer notifications.
- **S12: Authorization delays.** https://www.oig.hhs.gov/reports/all/2022/some-medicare-advantage-organization-denials-of-prior-authorization-requests-raise-concerns-about-beneficiary-access-to-medically-necessary-care/. 2022 Medicare Advantage review; inappropriate denials can delay access.

Research limitations: no clinician interviews or live product trials have been conducted. Some evidence comes from provider/community settings rather than insurer operations. Older studies support problem existence, not 2026 prevalence. All product scores, feed freshness goals, operational thresholds, baseline values, pilot design and pricing are explicit assumptions.
