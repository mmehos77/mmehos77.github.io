# Symptom Sorter (FM-51 patroller scope)

An offline wilderness first aid reference for Indian Peaks Wilderness Alliance (IPWA) patrollers.
You tap the signs and situation you see; the app ranks possible causes and shows the patroller-level treatment for each.

**Live app:** https://mmehos77.github.io

> Reference aid only, not a diagnosis. Follow your training, IPWA procedures and medical direction.
> The content has not been reviewed by a physician or medical director.

## Source

All medical content comes from one publication:
*Emergency Medical Services Protocols and Procedures*, Field Manual #51, National Park Service and U.S. Forest Service, 2025 edition.

- FM-51's protocols are split into 59 conditions (for example AMS, HAPE and HACE within Altitude Illness). Each condition's signs are quoted from FM-51 with page numbers.
- Possible spinal injury comes from FM-51's procedures 1400 (Spinal Examination) and 1410 (Spinal Motion Restriction), since FM-51 has no spinal-injury protocol.
- Treatment shows only steps FM-51 allows for any provider or the EMR (Emergency Medical Responder) level, plus steps with no level that FM-51 allows "if within the provider's scope of practice" (p. 13). Steps for EMTs and above are left out.
- Where FM-51's medication table (p. 8) limits responders more than a flowchart does, the stricter limit is shown.

## Using the app

- **Signs** are grouped in assessment order: scene size-up, primary assessment (life threats, airway, breathing, circulation, mental status), then secondary assessment (vital signs, a head-to-toe exam, and what the patient reports). Group names and chip wording are the app's own; FM-51's exact wording shows when you open a condition.
- **Typing or dictating:** the search box accepts everyday phrases, such as "short of breath, weak pulse, bleeding on right leg," and suggests matching signs to tap. It skips phrases preceded by "no," "not" or "denies." The phrase list is the app's own wording, about 1,400 phrases, not FM-51's. It works offline, and iPhone dictation works in the box.
- **Ranking:** rarer signs count more; a condition that explains everything you entered ranks above one that matches only part of it; ties go to the more urgent condition. The score is not a probability.
- **Browse** lists every condition under its FM-51 protocol, in the manual's order.
- **About** explains the ranking, the urgency and treatment tags, and includes FM-51's SAMPLE and OPQRST checklists (p. 107).
- **Picks are kept** after closing the app until you tap **Clear all**. Clear them before starting on a new patient.

## Installing on a phone

1. Open https://mmehos77.github.io in Safari (iPhone) or Chrome (Android) while you have Wi-Fi or cell service.
2. Tap Share, then **Add to Home Screen**.
3. After that first visit the app works with no signal.

## Files in this repository

| File | Purpose |
|---|---|
| `index.html` | The whole app, including all FM-51 data |
| `sw.js` | Offline helper: fetches the newest version when online, uses the saved copy when offline |
| `manifest.webmanifest` | App name and icons for "Add to Home Screen" |
| `icon-192.png`, `icon-512.png`, `apple-touch-icon.png` | App icons |

## Updating

1. Replace `index.html` with the new version.
2. In `sw.js`, raise the number in `VERSION` (for example `ss-fm51-2025-v21` to `-v22`) and replace that file too.
3. Commit to `main`. GitHub publishes within a few minutes (watch the Actions tab for a green check).
4. Phones get the new version the next time the app opens with a signal.
