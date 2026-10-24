# Form backend: Luxury Tours Canada lead capture

Kathy's decision (2026-10-23): LTC leads land in the SAME Google Sheet as the
Arkipelago lead tracker, on their own tab. One place to look, one tool to open.

```
Sheet:  13w_Tvph-NJQseB_MeBFRhCuMAr3JA4fLStnSXmDCQTo   (the Arkipelago lead tracker)
Tab:    Leads Canada                                   (new tab, LTC only)
Notify: kathyhingan@gmail.com                          (personal email alert per lead)
```

Two guardrails that make the shared sheet safe:

1. **New tab, never the Leads tab.** The LTP digest and cadence scripts read the
   `Leads` tab only (fill-colour buckets and Gmail, per the schema inventory).
   LTC rows land in `Leads Canada`, so LTP bucket logic, the five-colour scheme,
   and the daily digests are untouched, and LTC spam stays in its own tab.
2. **New STANDALONE Apps Script project, never the LTP script.** The LTP capture
   script is live production infra and never gets edited or redeployed. Create
   this one at script.google.com > New project (standalone). It opens the shared
   sheet by ID and deploys its own `/exec` URL.

## 1. Create the tab (Kathy, 3 minutes)

1. Open the Arkipelago lead tracker (the one whose `Leads` tab takes LTP leads).
2. Add a tab named exactly `Leads Canada`.
3. Row 1 headers, exactly these 19 columns in this order. The script writes the
   first 17; the last 2 are your manual cadence columns, blank by default, the
   same two the LTP tab carries (schema inventory recommends 19 so the manual
   workflow feels identical from day one). Columns can be appended later
   without touching Code.gs because appendRow writes from the left.

```
Received | Form Timestamp | Name | Email | Journey Type | Phone | Dates |
Group Size | Message | Page | Source | Quiz Who | Quiz Draw | Quiz Pace |
Quiz Dest | Quiz Luxury | Quiz Archetype | Last touch | Next scheduled call
```

4. Freeze row 1, fill the header row rgb(0.953, 0.953, 0.953), matching the LTP
   Leads tab. No data validations, no conditional formats: the LTP model carries
   lead status as manual row fills only.

## 2. Paste the script (Kathy)

script.google.com > New project (standalone, NOT opened from the sheet) > paste
`Code.gs` below > Save. The sheet ID below is already the shared tracker: no
editing needed.

```javascript
// Luxury Tours Canada lead capture. Standalone script: appends to the
// "Leads Canada" tab of the shared Arkipelago lead tracker and emails
// kathyhingan@gmail.com. Does not touch the LTP script, the Leads tab,
// or any LTP automation.

var SHEET_ID = '13w_Tvph-NJQseB_MeBFRhCuMAr3JA4fLStnSXmDCQTo';
var TAB_NAME = 'Leads Canada';
var NOTIFY   = 'kathyhingan@gmail.com'; // notification to Kathy's personal email

function doPost(e) {
  try {
    var p = e.parameter || {};
    // Server-side phone normalization, defense in depth. Sheets treats a
    // leading + as a formula and drops the value. site.js already converts
    // it client-side; this covers testAppend and any direct POST. Must run
    // before the row array is built.
    if (p.phone && String(p.phone).indexOf('+') === 0) {
      p.phone = '00' + String(p.phone).slice(1);
    }
    var now = new Date();
    var tz  = Session.getScriptTimeZone();

    // First 17 columns of "Leads Canada". Last touch and Next scheduled
    // call are Kathy's manual columns and are left blank by the script.
    var row = [
      Utilities.formatDate(now, tz, 'yyyy-MM-dd HH:mm:ss'), // Received (sheet time)
      p.timestamp     || '',                                // Form Timestamp (client ISO)
      p.name          || '',
      p.email         || '',
      p.journey_type  || '',                                // segment tag
      p.phone         || '',
      p.dates         || '',
      p.group_size    || '',
      p.message       || '',
      p.page          || '',                                // page tag
      p.source        || '',
      p.quiz_who      || '',
      p.quiz_draw     || '',
      p.quiz_pace     || '',
      p.quiz_dest     || '',
      p.quiz_luxury   || '',
      p.quiz_archetype|| ''
    ];

    var ss = SpreadsheetApp.openById(SHEET_ID);
    var sheet = ss.getSheetByName(TAB_NAME);
    if (!sheet) throw new Error('No "' + TAB_NAME + '" tab on the shared tracker. Create it first (19 headers, script fills 17).');
    sheet.appendRow(row);

    var subject = 'LTC Lead: ' + (p.name || 'unnamed') +
      (p.journey_type ? ' (' + p.journey_type + ')' : '') +
      (p.page ? ' from ' + p.page : '');
    var body =
      'New Luxury Tours Canada inquiry\n\n' +
      'Name: '        + (p.name || '') + '\n' +
      'Email: '       + (p.email || '') + '\n' +
      'Journey type: '+ (p.journey_type || '') + '\n' +
      'Phone: '       + (p.phone || '') + '\n' +
      'Dates: '       + (p.dates || '') + '\n' +
      'Group size: '  + (p.group_size || '') + '\n' +
      'Page: '        + (p.page || '') + ' (source: ' + (p.source || '') + ')\n' +
      'Message:\n'    + (p.message || '') + '\n\n' +
      'Respond within 24 hours (brand guarantee).';

    MailApp.sendEmail(NOTIFY, subject, body);

    return ContentService.createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet() {
  return ContentService.createTextOutput(JSON.stringify({ ok: true, alive: true, ts: new Date().toISOString() }))
    .setMimeType(ContentService.MimeType.JSON);
}

// Run once from the editor to prove the tab write works before wiring the site.
function testAppend() {
  doPost({ parameter: {
    name: 'TEST LTC', email: 'test@example.com', journey_type: 'Private Journey',
    phone: '+1 604 555 0142', dates: 'September 2027', group_size: '2 adults',
    message: 'testAppend smoke test', page: '/test/', source: 'ltc-test',
    timestamp: new Date().toISOString()
  }});
}
```

## 3. Deploy (Kathy)

In the NEW project only: Deploy > New deployment > type: Web app > Execute as:
Me > Who has access: Anyone > Deploy > approve the mail and sheets permissions
when asked > copy the `/exec` URL.

## 4. Wire the site

Replace the token in every page that carries a form:

```
grep -rl "LTC_APPS_SCRIPT_DEPLOY_TOKEN" .
```

Find and replace `LTC_APPS_SCRIPT_DEPLOY_TOKEN` inside the URL with the real
deployment key (the part between `/macros/s/` and `/exec`). Today that is ONE
occurrence, the form action in index.html (home is the only page with a form;
the MICE brief form is a later capture surface and will add its own action).
The site is static, so no rebuild is needed after.

## 5. Verify end to end (the only proof)

The form shows its success message whether or not a row lands, so the readback
is the proof, not the toast:

1. Run `testAppend` from the editor. Check the `Leads Canada` tab gets the row
   and kathyhingan@gmail.com gets the email. Confirm the `Leads` tab did NOT
   change. Delete the test row afterwards.
2. Open the live homepage, fill the real form with real values, submit.
3. Read the `Leads Canada` tab back: the row must carry the exact values, the
   page tag, and the journey type, with Last touch and Next scheduled call
   left blank for you. Check the Gmail notification arrived.
4. If a row does not land: the payload keys and the deployed script's
   `e.parameter` list must agree. Any new field means editing this script AND
   redeploying as a New version (Manage deployments > pencil > New version),
   confirming the `/exec` URL did not change, and re-checking the site.

## Notes

- The form posts through a hidden iframe (`target="formSink"`), the same
  pattern the LTP stack uses, so the POST survives the Apps Script redirect
  without CORS work.
- Submissions are tagged by `page` (per-page hidden input) and by segment
  (`journey_type` plus the hidden quiz fields kept for shape parity with the
  LTP lead contract). Each page's conversion stays measurable.
- Column shape vs LTP: the live Leads tab carries 23 columns; the 7 absent here
  (Segment, Children, Pets, Company, Budget, Last touch, Next scheduled call)
  are either manual-enrichment columns the LTC home form does not collect, or
  the two manual cadence columns now restored as headers 18 and 19. Full
  cross-check in docs/lead-sheet-schema-2026-10-23.md.
- Analytics IDs are still `[GA ID TBD]` / `[CLARITY ID TBD]` in every head.
  Insert NEW IDs when created; never reuse the Arkipelago IDs.
- Domain: luxurytourscanada.com is PURCHASED. All canonical, og:url, and schema
  URLs already point at it. CNAME file is in the repo for GitHub Pages,
  matching the Arkipelago hosting pattern.
