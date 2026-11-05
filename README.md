# CareFlow

**HiLabs APM Case Submission 2026–27**  
**Akshath Murali · ME23B010**

Open index.html (or CareFlow_Workbench.html) directly in a modern browser. No installation, server, internet connection, API key or build step is required. The same file powers the ChatGPT Site.

## Start here
Choose User journeys in the sidebar or Play a journey in the top bar. Select one of five patient journeys. Follow the highlighted control or click Do this step. Prompts explain the decision. Each journey runs in a temporary sandbox and restores your previous workspace when you finish or exit.

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

Your changes are stored only in localStorage in the browser under carethread-v1. Hosted and file:// copies have separate storage. Back up through Downloads to move your workspace. If browser storage is restricted, the app remains usable for the session and displays a storage warning. Do not put real patient data into this demonstration.

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

## Live website
https://carethread-clinical-workbench.pranavbhatnagar17.chatgpt.site

## Final submission
- `slides/Slide_01.png` through `slides/Slide_12.png`: individual 2400 × 1350 images.
- `documents/CareFlow_Presentation.pdf`: those exact images merged in order. Embedded pixels verified equal to the PNG originals.
- `documents/CareFlow_Synthetic_Patients.xlsx`: five fictional patients across 13 patient-linked dataset groups.
- `documents/CareFlow_Editable_Slides.pptx`: optional editable deck.
- `index.html`: final standalone workbench, including guided user journeys.

## Vercel
Import this GitHub repository in Vercel. Use **Other** as the framework preset, repository root as root directory, no build command, and `.` as output directory if prompted. The committed root `index.html` is ready to serve; no secrets or environment variables are needed. No Vercel deployment has been created as part of this submission.

## Editing
Edit `source/app.js`, `source/style.css`, or `data/synthetic-data.json`, then run `python rebuild.py` to update root `index.html`. The rebuild uses only Python standard libraries. The static app needs no Python server or installed packages to run.

## Brand attribution
HiLabs logo retrieved from its official website: https://www.hilabs.com/new-website/icon/footer-logo-black.svg . Slide blue #2A6AF1 and navy #031335 follow official website CSS. Use is for this academic case submission and does not imply company endorsement.
