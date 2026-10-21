# Form backend: Luxury Tours Canada lead capture

Replicates the LTP stack exactly: the site form posts to a Google Apps Script
web app, the script appends the row to a Google Sheet, and it emails a
notification to Kathy's personal Gmail, tagged by page and segment. Nothing here
reuses the Arkipelago sheet, script, or deployment. Do not point the LTC form at
the LTP `/exec` URL.

## 1. Create the sheet (Kathy, 2 minutes)

1. Sheets: new spreadsheet, name it `LTC Leads`.
2. Rename `Sheet1` to `Leads`.
3. Row 1 headers, exactly these 17 columns in this order:

```
Received | Form Timestamp | Name | Email | Journey Type | Phone | Dates |
Group Size | Message | Page | Source | Quiz Who | Quiz Draw | Quiz Pace |
Quiz Dest | Quiz Luxury | Quiz Archetype
```

4. Copy the spreadsheet ID from the URL (the long string between `/d/` and `/edit`).

## 2. Paste the script (Kathy)

Sheets > Extensions > Apps Script > delete the stub > paste `Code.gs` below >
replace `SHEET_ID` with the ID from step 1 > Save.

```javascript
// Luxury Tours Canada lead capture. Writes to the LTC Leads sheet and
// emails kathyhingan@gmail.com. Do not reuse any Arkipelago script or sheet.

var SHEET_ID = 'PASTE_THE_LTC_LEADS_SHEET_ID_HERE';
var NOTIFY   = 'kathyhingan@gmail.com'; // notification to Kathy's personal email

function doPost(e) {
  try {
    var p = e.parameter || {};
    var now = new Date();
    var tz  = Session.getScriptTimeZone();

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

    var sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName('Leads');
    if (!sheet) throw new Error('No Leads tab on the LTC Leads sheet');
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

// Run once from the editor to prove the sheet write works before wiring the site.
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

Deploy > New deployment > type: Web app > Execute as: Me > Who has access:
Anyone > Deploy > approve the mail permission when asked > copy the `/exec` URL.

## 4. Wire the site

Replace the token in every page and doc:

```
grep -rl "LTC_APPS_SCRIPT_DEPLOY_TOKEN" .   # should list 18 index.html files
```

Find and replace `LTC_APPS_SCRIPT_DEPLOY_TOKEN` inside the URL with the real
deployment key (the part between `/macros/s/` and `/exec`). One occurrence per
page, in the form action. Then redeploy nothing: the site is static.

## 5. Verify end to end (the only proof)

The form shows its success message whether or not a row lands, so the readback
is the proof, not the toast:

1. Run `testAppend` from the editor. Check the Leads tab gets the row and
   kathyhingan@gmail.com gets the email. Delete the test row afterwards.
2. Open the live homepage, fill the real form with real values, submit.
3. Read the Leads tab back: the row must carry the exact values, the page tag,
   and the journey type. Check the Gmail notification arrived.
4. If the row does not land: the payload keys and the deployed script's
   `e.parameter` list must agree. Any new field means editing Code.gs AND
   redeploying as a New version (Manage deployments > pencil > New version;
   the URL stays the same).

## Notes

- The form posts through a hidden iframe (`target="formSink"`), the same
  pattern the LTP stack uses, so the POST survives the Apps Script redirect
  without CORS work.
- Submissions are tagged by `page` (set per page in the hidden `page` input)
  and by segment (`journey_type` plus the hidden quiz fields kept for shape
  parity with the LTP lead sheet). Each page's conversion stays measurable.
- Analytics IDs are still `[GA ID TBD]` / `[CLARITY ID TBD]` in every head.
  Insert NEW IDs when created; never reuse the Arkipelago IDs.
