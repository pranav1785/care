# Interface decisions

Public reference review, 6 November 2026:
- VS Code custom layout: https://code.visualstudio.com/docs/configure/custom-layout . Reused the idea of persistent tabs, a secondary context panel, an optional notes dock, split/focus presets and resizable zones. Patient identity stays fixed and cross-patient editing is excluded.
- Linear inbox: https://linear.app/docs/inbox . Inspected its public screenshot and documented notification behavior. Borrowed restrained row density, clear unread state, a navigation rail and separation of attention from task completion.
- Salesforce Health Cloud enhanced timeline: https://trailhead.salesforce.com/content/learn/modules/health-cloud-data-displays/add-objects-to-health-timeline . Borrowed typed chronological events, expandable source evidence and event filters.
- Intercom inbox: https://www.intercom.com/help/en/articles/7911926-customize-the-inbox-to-suit-you-and-how-you-work-best . Borrowed a conversation/context relationship and configurable workspace regions.

CareFlow uses original CSS, SVG icons and JavaScript. Its warm neutral background, forest-green accents, typography, thin dividers, open spacing and limited filled surfaces are original choices. Clinical uncertainty gets a text label and evidence, rather than a decorative confidence score. Charts represent the actual five-member source snapshot or logged activity.

The requested prior bus-tracking/advanced human-factors design was not located in the accessible recent project/chat inventory. The described prompted/highlighted guided journey behavior was implemented directly. The accessible Explain Kivi PS chat contained problem-statement discussion, not a visual design, and was not used as an interface reference.
