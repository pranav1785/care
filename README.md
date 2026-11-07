# CareFlow Case Management Workbench

Open index.html (or CareFlow_Workbench.html) directly in a modern browser. No installation, server, internet connection, API key or build step is required. The same file powers the ChatGPT Site.

## Start here
Choose User journeys in the sidebar or Play a journey in the top bar. Select one of five patient journeys. Click the highlighted control or use the single Next button, which performs that same action and advances. The prompt follows the target and scrolls it into view. Dismiss the opening invitation to explore independently. Each journey runs in a temporary sandbox and restores your previous workspace when you finish or exit.

## Main workflows
- Overview: five-member queue, actual counts, source event chart and contact-time reminders.
- Work queue: search and filter by priority, plan and case state. Priority reasons are explicit.
- Patient: persistent tabs, overview, timeline filters, care plan, medication evidence and original source documents.
- Outreach: permission checks, contact routes/outcomes, scenario examples and factual notes.
- Tasks/referrals: owners, due dates, stages and completion evidence. Sent/accepted differs from received/verified. Unavailable service remains unmet.
- Notes: member-bound drafts, deterministic source-based template assistance, review, signature and amendment history.
- Case management: state changes, reasoned closure/reopen, supervisor-role transfer and priority overrides with reason/expiry.
- Workspace: light/dark switch, drag/reorder patient tabs, pin tabs, context resizing, note-dock resizing, Focus/Split-note/Context layouts, keyboard equivalents, reset layout and compact mode.
- Notifications: read/unread, open case and session snooze. Acknowledgment does not complete tasks.
- Insights: actual local demo contacts, connections, tasks and signed notes. Baselines/targets remain explicitly hypothetical.
- Downloads: HTML, complete project ZIP, original XLSX annex, dataset JSON, case JSON, task/queue CSV, notes through case exports, activity CSV, backup/restore, pre-build PDF and specification. Browser print can save a care plan as PDF.

## Data and storage
Five original fictional members from the supplied annex. Demonstration date: Monday 9 November 2026, 08:00 US Eastern. Source observations retain their dates and limitations. Dates with offsets in source JSON are original timestamps; the spreadsheet shows local Eastern wall time.

Your changes are stored only in localStorage in the browser under careflow-workspace-v2. The legacy carethread-v1 record is retained, with a recovery copy when storage allows. Hosted and file:// copies have separate storage. Back up through Downloads to move your workspace. If browser storage is restricted, the app remains usable for the session and displays a storage warning. Do not put real patient data into this demonstration.

## Working demo and integration boundaries
This is a fully interactive synthetic, browser-local application, not a production clinical system. Calls, messages, external referrals, bookings, staff authentication and AI are simulated. Template-assisted notes are deterministic and labeled. No live healthcare feeds, real authentication, backend database, external messaging or LLM service is connected. Data never leaves the browser through these simulated actions. Export and browser printing are real local operations. Hosting access follows ChatGPT Sites owner-private access.

Source-based safety checks support the demonstration but are not clinically validated. The priority scheme, baseline metrics, service levels and pricing in the pre-build documents are hypotheses. No emergency monitoring service is provided.

## Files
- index.html: self-contained app including CSS, JavaScript, synthetic data and downloadable artifacts.
- source/app.js and source/style.css: editable implementation source.
- data/synthetic-data.json: original generated scenario data and dataset records.
- documents/: specification, reference guide, XLSX annex, PDF and editable PowerPoint.
- DESIGN_NOTES.md: observed reference patterns and original implementation decisions.
- QA.md: verification scope and limitations.

All interface code is original. VS Code, Linear, Salesforce Health Cloud and Intercom informed interaction patterns. No proprietary application code or brand assets were copied.


# CareFlow v2 — upgrade guide

## What changed

This release extends the original vanilla JavaScript workbench. It retains the five original synthetic patients, source annex, manual outreach, care plans, tasks/referrals, signed-note history, original guided journeys, workspace layouts, dark mode, exports and local backups. No framework migration or external clinical service was introduced.

| Module | Working capability | Important boundary |
| --- | --- | --- |
| CareLens | Member-specific questions about priority, medications, fills, appointments, changes, contact history, social context, actions and stale sources. Click evidence references to inspect original rows or current local records. | Deterministic intent matching, not an open-ended LLM. Unsupported questions and treatment decisions abstain. |
| CareLens changes | Comparison with the most recent meaningful recorded interaction; failed attempts do not become successful contact. Earlier events received later are labeled. | Historical contact dates retain day precision. Missing facts remain unknown. |
| CareOps AI | Explicit simulated calls, English/Spanish scripts, five branches, next-response control, pause/resume/interruption, transcript and findings review. | No real calls, speech recognition, emergency response or live AI. Permission, route, contact window and caregiver scope are reviewed first. |
| CareMesh | Owned actions, external parties, dependencies, next-review dates, evidence, history and Waiting on Others. | Accepted or scheduled referrals do not establish service delivery. Dependencies cannot cross members or form a cycle. |
| OutcomeLoop | Intervention-linked feedback, five responses, source/verification labels, renewed follow-up and reviewed goal progress. | Feedback is patient/caregiver-reported; it does not independently verify delivery or automatically achieve a goal. |

## Best demonstration

1. Open **Command Center**, then **Play the closed-loop story**.
2. Open Morgan and ask CareLens about unresolved commitments; inspect the evidence.
3. Read **Since last interaction** and the earlier-event update.
4. Prepare AI outreach, explicitly review the fictional permissions and play the practical-barrier branch.
5. Read the findings, confirm review, approve a follow-up and an unsigned draft.
6. Inspect **Waiting on others**. Housing support remains accountable to the internal nurse.
7. Open the housing intervention’s patient feedback and report that the service did not arrive.
8. Return to the nurse workspace: the intervention, goal, timeline, attention reason and follow-up reflect the report.
9. Finish to restore your original workspace. This journey is temporary and is never saved over existing work.

The five original guided journeys are also available. Every journey uses one Next button, or you can activate each highlighted control directly. Next performs the same real, validated demo action and advances. The travelling prompt scrolls each control into view. The opening tutorial invitation can be dismissed for independent exploration; dismissal is remembered in the current browser tab. Each walkthrough still restores your prior workspace.

## Using the upgraded workspace

**Command Center:** counts reflect the actual five-member workspace. Quick filters cover priority, due today, overdue, waiting, outreach, review and changes. Priority is explainable review urgency; it is separate from the preferred time to call. The demo clock starts November 9, 2026, 08:00 Eastern and moves forward only when explicitly advanced.

**Patient workspace:** retains stable member/case identity and original tabs. New tabs are Since last interaction, AI outreach and Goals & outcomes. Questions and drafts remain member-bound. Open multiple patients, resize context/notes, pin/reorder tabs or use a focus layout.

**Simulated outreach:** choose a supported branch: routine follow-up, person requested, clinical concern, no answer or practical barrier. Review route/permission/identity first. Jordan’s evening window, Morgan’s 14:00 window, Casey’s caregiver scope and Riley’s disconnected number remain explicit. No-answer is not an assessment. Findings become an owned action or unsigned note only after review. A clinical concern is labeled for protocol-governed qualified review, never silently treated as an ordinary completed call.

**Action review:** retain an internal owner even when waiting on an agency. Record a review date, dependencies and dated, attributable evidence. An action completed, service delivered and patient goal achieved are different facts. An unresolved dependency blocks completion. Source verification remains visible.

**Patient feedback:** open it from a specific intervention. The lightweight page supports helped, partly helped, still need help, not received and speak to a person. Casey may use the authorized caregiver scope. A repeat click with the same submission ID does not duplicate the report. Negative feedback creates/reopens one linked follow-up. A later report does not erase earlier history. Goals require nurse review and cannot be marked achieved with linked open actions or unmet feedback.

**Persistence:** v2 state uses a versioned browser-local envelope. Existing legacy data is migrated without overwriting the legacy key. Corrupt/newer imports are rejected. Export a backup before moving between the hosted site and downloaded HTML; each origin has separate storage. A patient feedback link is a same-browser synthetic demonstration, not a secure cross-device portal.

## Architecture and data

- `source/app.js`: retained workbench and original interactions, with small compatibility and source-download additions.
- `source/upgrade-core.js`: deterministic state rules, provenance, calls, feedback, goals, validation and migration.
- `source/upgrade-ui.js`: adapters that add the new views to the existing shell and shared state.
- `source/upgrade.css`: incremental layout and responsive feedback styling.
- `data/synthetic-data.json`: unchanged original annex, five fictional records and 17 dataset groups.
- `rebuild.py`: standard-library Python rebuild of the self-contained HTML; no installation needed.
- `tests/core.cjs`: portable Node core regression checks; run `node tests/core.cjs`.

All workflows use the same member-bound workspace. Exports and downloads are real local operations; external bookings, messages, clinical feeds, authentication and AI are simulated. No credentials or hosting identity are included in the user ZIP. No production PHI, emergency monitoring, real voice service or shared backend is implemented. Optional speech and campaign-scale experiments remain deferred.

## Verification

See QA.md and tests/results.json for the executed checks. The release was verified with core regression tests, all five original browser journeys and the new closed-loop browser journey. The source ZIP was extracted and rebuilt to verify the delivered structure. Browser checks cover the synthetic demo only; they do not establish clinical validation or production readiness. Earlier decks and documents in documents/ remain the original submission artifacts, not revised descriptions of every v2 capability.
