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
