# CareFlow v2 verification report

This release extends the existing workbench without a framework migration. All five source patient records and the original annex are retained.

## Executed checks
- 51/51 deterministic core regression checks passed: legacy migration and retention, evidence-grounded member-specific Q&A, missing-evidence abstention, last meaningful contact, late-arriving events, same-clock event ordering, clock/windows/route/permission restrictions, five call branches, Spanish script, interruption, reviewed/idempotent updates, member-safe dependencies, circular-dependency rejection, dated task evidence, all five feedback choices, caregiver scope, closed-loop follow-up, goals and reload.
- All five original guided patient journeys completed in the upgraded browser build, including outreach, actions and reviewed/signature flows. Each restored its original workspace.
- New ten-step Morgan closed-loop browser journey completed. Permission and review omissions were blocked. Reviewed simulated outreach produced an owned follow-up and unsigned draft. Not-received housing feedback updated intervention outcome and goal; the linked follow-up remained open. Finishing restored the original workspace.
- CareLens answer survived browser reload. CL-1 citation opened the original Avery discharge evidence, preserving both conflicting doses without selecting treatment.
- Normal patient feedback (outside a temporary journey) survived reload and appeared in the nurse outcome view.
- Desktop workspace inspected at 1440 × 900. Patient feedback inspected at 390 × 844. Temporary viewport overrides were reset.
- Simulated call permission omission blocked start. A permitted four-turn practical-barrier call completed and displayed its transcript/findings.
- In-app complete project ZIP downloaded successfully. Delivered ZIP CRC, expected upgraded sources, tests, data and documents checked; extracted package rebuilt successfully using Python standard libraries.
- JavaScript syntax and portable packaged regression tests passed. No new browser console error was observed after the initial development error was fixed.

## Retained baseline
Original source, annex data and workflows were audited before changes. Baseline source hash on GitHub main was app.js blob 1d19d7b8d40ea52a82771a886c47e3d89989aba7. Existing source was extended through small compatibility edits and separate upgrade modules. Original source data and XLSX were not rewritten. Local-storage migration retains legacy state and a recovery copy when available.

## Verification limits
The browser disallows file:// navigation, so direct double-click execution was not browser-tested. The same standalone file was served locally; the extracted source package was rebuilt and checked. This is a synthetic browser-local prototype: deterministic Q&A, simulated calls/coordination, same-browser feedback, no backend/real authentication/PHI/clinical integration. No clinical validation, real emergency monitoring, immutable compliance audit or cross-device portal is claimed. Optional speech and campaign-scale lab are deferred. Earlier presentation documents are retained historical submission artifacts.


## Tutorial interaction update — November 7, 2026

- Opening invitation and Play a journey highlight displayed on entry. Dismiss removed both; reload in the same tab retained dismissal. The invitation preference is separate from patient data and backups.
- All five original patient journeys completed through a single Next button after the update. No Show this step / Return / Skip button is present in the active prompt.
- Closed-loop walkthrough completed through all 25 atomic actions using only Next, and again by clicking the actual highlighted controls. Buttons, checkboxes, patient feedback submission and read/acknowledge summaries all advance automatically after their validated action.
- Phone-size (390 × 844) closed-loop journey completed using Next. The travelling prompt and highlighted permission checkbox did not overlap in the inspected modal. Temporary viewport override was reset.
- Both completion paths restored the original workspace. No browser console errors were recorded during final checks. Existing source data and core clinical rules were unchanged.
- Source syntax, archive integrity and extracted rebuild checked. This remains the synthetic browser-local application described above.


## Command Center entry and content visibility update

- Fresh app entry, a previously saved User Journeys view, and an older #home/journeys entry URL open in Command Center. Explicit intervention feedback links retain their dedicated purpose. Patient records, tabs, drafts and saved work are retained.
- Removed the green Morgan showcase banner and duplicate dashboard launch control. The single top-bar Play a journey control starts the closed-loop tutorial directly. Its invitation can be dismissed without navigating away from Command Center. The five patient tutorials remain available through deliberate sidebar navigation.
- All 25 closed-loop steps completed at desktop size and again at 390 × 844. DOM geometry checks at every step confirmed the highlighted control was visible and did not overlap the tutorial prompt. All five patient journeys also completed with target visibility/non-overlap checks (81 steps).
- If there is insufficient adjacent space, a reserved guide lane reduces the workspace/dialog viewport instead of covering its content. The relevant control scrolls into view. Review-dialog focus no longer scrolls its highlighted checkbox away; returning from patient feedback opens the outcomes with the notes dock closed.
- Reload after leaving the app on User Journeys returned to Command Center. Banner count was zero, one top-bar launcher was present, and dismissing the introduction removed the highlight. No browser console errors were observed. Browser viewport was restored.
- Source syntax, ZIP integrity, original synthetic data equality and extracted rebuild checked. Core rules and source patient facts were not changed.
