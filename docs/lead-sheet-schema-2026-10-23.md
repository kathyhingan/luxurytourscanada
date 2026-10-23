# Lead sheet schema: live LTP Leads tab vs the planned LTC Leads sheet

Inventory read 2026-10-23 by am-ltc-bot. Read-only Sheets API against the live
Arkipelago tracker (personal token, no writes). Purpose: pin the exact sheet
shape the LTC capture stack must replicate, before instantiation. This is prep
for packet item 3, not a build step. Nothing was created.

## Live LTP Leads tab, read 2026-10-23

- Spreadsheet 13w_Tvph-NJQseB_MeBFRhCuMAr3JA4fLStnSXmDCQTo, tab `Leads`.
- Grid: 26 columns wide, 23 used, frozen row 1, header fill light gray
  rgb(0.953, 0.953, 0.953).
- Data shape: zero data validations, zero conditional formats on the tab. Lead
  status lives only in manual row fills on the Name cell, per the 5-color
  scheme in the tracker conventions (white = new or closed-won, cream =
  pending, soft pink = lost, bold orange = proposal sent, blue = B2B).
- Headers, exact order (23). The six quiz headers on the live sheet are
  spelled Quiz + a dash + the label (an em dash on the LTP sheet); the LTC
  plan spells every header dash-free by rule:

```
Timestamp | Name | Email | Journey Type | Dates | Group Size | Message |
Quiz Who | Quiz Draw | Quiz Pace | Quiz Destination | Quiz Luxury |
Quiz Archetype | Source | Phone | Segment | Children | Pets | Company |
Budget | Page | Last touch | Next scheduled call
```

- Sibling tabs on the tracker: Resorts and Hotels Partners, Interactive Map,
  Explorer Map, Partner DB Raw (2026-10-15). Only the Leads tab is in scope
  for the LTC v1 capture stack.

## Planned LTC Leads sheet (docs/form-backend.md): 17 columns

```
Received | Form Timestamp | Name | Email | Journey Type | Phone | Dates |
Group Size | Message | Page | Source | Quiz Who | Quiz Draw | Quiz Pace |
Quiz Dest | Quiz Luxury | Quiz Archetype
```

Verified: the Code.gs row array in form-backend.md writes exactly this order,
so header order and append order agree. Two deliberate improvements over LTP:
the single LTP Timestamp column splits into Received (server time) plus Form
Timestamp (client ISO), which separates sheet latency from submit time; and
Phone moves next to Journey Type to match the form order.

## Delta: 7 LTP columns absent from the LTC plan

| LTP column | Live use | In LTC plan |
|---|---|---|
| Segment | manual qualification tag | dropped, Journey Type carries the form segment |
| Children | manual enrichment | dropped, home form does not collect it |
| Pets | manual enrichment | dropped, home form does not collect it |
| Company | manual enrichment | dropped, home form does not collect it |
| Budget | manual enrichment | dropped, home form does not collect it |
| Last touch | manual cadence ops column | dropped |
| Next scheduled call | manual call-scheduling column | dropped |

Cross-checked against the LTP automation: no script reads these 7 columns.
daily_digest.py and cadence_engine.py work from fill colors and Gmail
history; ltp_build_snapshot.py derives its Last touch from Gmail, not the
sheet. They are manual Kathy columns.

Decision note for packet item 3 (Kathy, one binary at instantiation): create
the LTC sheet with the 17 planned columns, or 19 (add Last touch and Next
scheduled call back) so the manual cadence and call-scheduling workflow feels
identical to LTP from day one. Recommendation: 19. The 5 enrichment columns
stay out until a form or flow actually collects them; columns can be appended
later without touching Code.gs because appendRow writes from the left.

## Instantiation checklist (gated on packet item 3, unchanged build order)

1. New spreadsheet named `LTC Leads` in the account Kathy names, tab renamed
   `Leads`.
2. Row 1 headers: the 17 planned columns (or 19 per the decision above), in
   the form-backend.md order.
3. Freeze row 1, fill the header row rgb(0.953, 0.953, 0.953). No
   validations, no conditional formats (the LTP model carries status as
   manual fills only).
4. Copy the spreadsheet ID into Code.gs `SHEET_ID`, then follow form-backend.md
   sections 2 to 5 (script, deploy, wire, readback verification).
