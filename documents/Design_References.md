# Design references and review guide

Prepared 6 November 2026. These are public product references, not endorsements or completed usability evaluations. Public documentation and screenshots support the patterns described. No account signup, sales contact, or authenticated product testing was performed. Elation's detailed sample is gated.

## Ten references

| Reference | What to inspect | What we could borrow | Access / limitation |
|---|---|---|---|
| [VS Code](https://code.visualstudio.com/docs/configure/custom-layout) | Workspace flexibility: Documented tabs, editor groups and movable panels | Patient tabs, resizable context and notes dock | Public illustrated documentation. Avoid developer terminology and unrestricted multi-patient panes |
| [Linear](https://linear.app/docs/inbox) | Daily queue and attention: Illustrated inbox and notification workflows | Compact rows, clear unread states and detail view | Public illustrated documentation. Clinical urgency must remain distinct from unread status |
| [Intercom](https://www.intercom.com/help/en/articles/7911926-customize-the-inbox-to-suit-you-and-how-you-work-best) | Outreach workspace: Documented table/chat layouts and configurable sidebars | Queue, conversation and context visible together | Public illustrated documentation. Support conversation state is not a clinical case lifecycle |
| [Zendesk](https://support.zendesk.com/hc/en-us/articles/4408821259930-About-the-Zendesk-Agent-Workspace/) | Case operations: Documented unified ticket interface and channels | Case context next to interaction history | Public documentation and product visuals. Avoid treating healthcare cases as disposable support tickets |
| [Salesforce Health Cloud](https://trailhead.salesforce.com/content/learn/modules/health-cloud-data-displays/add-objects-to-health-timeline) | Patient timeline: Illustrated health timeline configuration | Event chronology and patient context | Public illustrated learning module. Reduce configuration complexity and keep action rationale explicit |
| [Pega Care Management](https://www.pega.com/industries/healthcare/care-management) | Payer workflow fit: Public care-management overview | Guided work, plan and task organization | Public product overview; deeper demo may require contact. Public page is insufficient to judge complete usability |
| [ZeOmega Jiva](https://www.zeomega.com/) | Payer breadth: Public payer-care platform overview | Coverage of care-management operations | Public overview; demo access may require contact. Use for domain comparison; authenticated workspace not inspected |
| [Healthie](https://help.gethealthie.com/article/173-overview-charting-within-healthie) | Documentation: Illustrated charting, prefill and intake reuse | Reusable facts and clear note lifecycle | Public illustrated help. Provider documentation differs from insurer coordination |
| [Elation Health](https://go.elationhealth.com/sample-chart) | Clinical chart reference: Sample-chart landing page only | Potential reference for longitudinal chart hierarchy | Form-gated sample; public landing page only. Detailed sample is form-gated; not reviewed or ranked on visual quality |
| [Canvas Medical](https://help.canvasmedical.com/articles/4129367510-commands-introduction) | Fast structured actions: Documented commands with explicit commit step | Draft versus committed action distinction | Public illustrated help. Exclude prescribing/order placement from our scope |

## Three directions to review

### A. Clinical workbench with optional flexibility (recommended)
VS Code supplies the workspace structure, Linear the queue density, and Health Cloud the clinical timeline. Start with a left navigation rail and daily queue, patient tabs across the center, patient record in the main area, a resizable right context panel and optional bottom notes dock. Use light neutral clinical content with restrained navy navigation. Keep the identity bar fixed. Persist panel preferences and allow Reset layout.

First version: reorder/pin patient tabs, resize the queue/context/notes zones, collapse zones, and choose Focus or Split-note preset. Only one active patient context can receive edits. Split-note mode shows that same patient's record and note. Dragging cannot hide identity or the safety/status strip. Minimum useful pane widths prevent unusable arrangements. Keyboard menu actions must offer equivalent control.

Later option: arbitrary docking and saved named layouts, only after usability testing. Moving every panel freely adds complexity and increases context errors. No cross-patient side-by-side editing in the first version.

### B. Inbox-first workspace
Intercom and Zendesk supply a persistent queue, central interaction view and right patient context. Best for frequent outreach. Less flexible but easier to learn. Keep a full patient summary available before starting contact.

### C. Clinical console
Salesforce Health Cloud and Healthie supply a stable chart-first layout, chronological events, assessment sections and task drawer. Best for complex review. Reduce navigation depth and put the next action above the fold.

## Proposed visual rules

Use 16px body text for the future desktop app, clear section labels, 8px spacing rhythm, minimum 44px primary control targets and WCAG 2.2 AA contrast as a design target. Red is reserved for a configured urgent clinical review state, amber for overdue work/data issues, blue for selected controls. Every status has text and an icon as well as color. Exact palette and typeface remain open.

Unread notification, overdue task, stale source and clinical urgency have distinct labels. Aggregate repeat events. Acknowledge does not complete a clinical task. Avoid percentages labeled AI confidence unless calibration supports them. Use Confirmed, Reported, Inferred, Conflicting and Unknown evidence labels instead.

## Review order

1. VS Code: decide how much layout flexibility feels useful.
2. Linear: decide queue density and notification handling.
3. Intercom: decide whether outreach should own the central workspace.
4. Salesforce Health Cloud: decide patient timeline hierarchy.
5. Healthie: decide note and assessment interaction.

Choose A, B or C, then choose light/dark navigation and preferred information density. This review authorizes no site generation or MVP implementation. The three wireframes in the deck illustrate information hierarchy only and do not lock the visual direction.
