# Form spam guard: staged, not applied (2026-11-06)

## What happened

The `Leads Canada` tab went from zero data rows to four on the morning of
2026-11-06. All four read as automated spam, not inquiries:

| Received | Name | Email | Phone | Page / Source | Read |
|---|---|---|---|---|---|
| 2026-11-06 5:42:53 | yosngwjzuw | tdtuydrj@formtests.info | 001-428-606-5762 | vuzfrkom / ltc-page | bot: every text field randomised, 9 seconds before the next |
| 2026-11-06 5:43:01 | ttxesxketk | klzqkqpi@formtests.info | 001-394-585-5595 | dmwzkzyw / ltc-page | same pattern, 50 seconds after the first |
| 2026-11-06 5:43:51 | eodqdnstvv | veizwnfp@formtests.info | 001-051-892-4965 | / / ltc-homepage | same pattern |
| 2026-11-06 6:41:15 | Michaelnex | alan-baker424245242@gmx.com | 84948218459 | / / ltc-homepage | link spam in the message field, no quiz fields |

Diagnosis: the first three carried the real per-page defaults of the hidden
`source` and `page` inputs while every other field was randomised, so the
sender parsed the rendered form and then randomised the text inputs. That
means a hidden honeypot input with an EMPTY default would be randomised too
and would catch this class of bot.

## Proposed guard (three edits, all small)

### 1. `docs/sitegen.py`, inside `JOURNEY_FORM`, directly after the
`quiz_archetype` hidden input

```html
        <div class="hp-field" aria-hidden="true">
          <label for="fieldWebsite">Website</label>
          <input type="text" id="fieldWebsite" name="website" tabindex="-1" autocomplete="off">
        </div>
```

### 2. `index.html`, same block, directly after its `quiz_archetype` hidden input

Identical markup to edit 1.

### 3. `assets/site.css`, appended

```css
.hp-field{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden}
```

Off-screen rather than `display:none`: many bots skip inputs they cannot lay
out, and the field has to look fillable to be worth filling.

### 4. `docs/Code.gs`, at the top of the `try` block in `doPost`

```js
    // Honeypot: a real browser never fills an off-screen "website" field.
    // Answer ok:true without writing a row or sending an alert, so the bot
    // sees success and does not retry.
    if (p.website) {
      return ContentService.createTextOutput(JSON.stringify({ ok: true }))
        .setMimeType(ContentService.MimeType.JSON);
    }
```

## Deploy order and why it is safe either way

- The client field alone changes nothing: the deployed `Code.gs` ignores
  unknown parameters.
- The `Code.gs` guard alone changes nothing harmful: `website` is empty on
  every real submission, so every real row still writes and still alerts.
- So either edit can ship first. `Code.gs` only takes effect after Kathy pastes
  it into the standalone LTC Apps Script project and redeploys the web app
  (Deploy > Manage deployments > edit > Version: New version > Deploy). The
  `/exec` URL stays the same, so no page change is needed with it.

## Not applied

Neither the honeypot field nor the `Code.gs` guard is in the live tree as of
2026-11-06. The capture path is untouched and proven. This doc is the
ready-to-apply spec, waiting on Kathy's go plus her redeploy.

## Also open for Kathy

The four spam rows are still on `Leads Canada`. Deleting live tracker rows is
Kathy's call; the safe mechanics if she wants them gone are in
`references/capture-e2e.md` (locate by exact cell value, re-read, assert,
`deleteRange` with `shiftDimension:"ROWS"`, full re-read).
