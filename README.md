# Symptom Sorter

An offline wilderness first aid reference for Indian Peaks Wilderness Alliance (IPWA) patrollers. You enter the signs you find, and it lists the conditions that best match, with first aid steps tagged by training level.

**Open the app:** https://mmehos77.github.io/wfa/

> Reference aid only, not a diagnosis. Follow your training, IPWA procedures and medical direction.
> The content has not been reviewed by a physician or medical director.

## What is on this site

| Address | What it is |
|---|---|
| `/wfa/` | **Symptom Sorter (WFA)**, the maintained app. See [`wfa/README.md`](wfa/README.md). |
| `/` (this folder) | A short page that forwards to `/wfa/`. |

The FM-51-only version that used to live at the main address was retired in November 2026. Its page now forwards to the WFA app, and its `sw.js` deletes the old app's offline copy from any device that still has it. The WFA app's offline copy is not affected.

## How the app works, briefly

- **Signs to conditions.** Each condition lists the signs its sources give. Conditions are ranked by how well your entered signs match. Rarer signs count for more.
- **Rules from the sources.** Some signs make a condition less likely, for example frostbite in rain. Some sign combinations raise urgency.
- **Every sign is cited.** Each sign links to its source, with a page number where the source has one.
- **Treatment tagged by training level:** *Any first aider*, *If WFA trained*, or *Evacuate or call for help*. Steps beyond WFA training are left out.
- **Works offline** once it has been opened online. Use **About → Check for update** to get a newer version.

## Sources

- **NPS / USFS Field Manual #51 (2025)**: the main source for conditions, signs and protocols.
- **Wilderness Medical Society Clinical Practice Guidelines**, all in *Wilderness & Environmental Medicine*.
  - **Full papers, with each quote checked against its page:**
    - Heat Illness 2024
    - Acute Altitude Illness 2024
    - Accidental Hypothermia 2019
    - Frostbite 2024
    - Spinal Cord Protection 2024
    - Burns 2025
  - **Published summaries only, quotes not page-checked:** the other topics, including hyponatremia, lightning, pit viper, anaphylaxis, drowning and ticks.
- **AHA / Red Cross first aid guidelines (2020, 2024) and AHA 2025 Adult Basic Life Support**: first aid and CPR steps.
- **Wilderness First Aid Scope of Practice (2012)**: the yardstick for what counts as *If WFA trained*.

## Files

| File | Purpose |
|---|---|
| `index.html` | Forwarding page to `/wfa/` |
| `sw.js` | Removes the retired FM-51 app's offline copy, then removes itself |
| `wfa/` | The app (see its README) |
| `tools/check_citations.py` | Checks every FM-51 quote in the app against the FM-51 PDF |
| `tools/check_wms.py` | Checks every full-paper WMS quote in the app against its PDF and page |

The PDFs are not kept in this repository, because the journal articles are copyrighted. Keep them on your own computer.

## Checking citations before a release

```
python3 tools/check_citations.py FM51.pdf wfa/index.html
python3 tools/check_wms.py wfa/index.html heat24=heat.pdf:112 alt24=alt.pdf:2 hypo19=hypo.pdf:47 fb24=fb.pdf:183 spine24=spine.pdf:78 burn25=burns.pdf:549
```

Both need `pdftotext` (poppler-utils) and print `OK` when every quote is found. For `check_wms.py`, the number after each PDF is its first printed page: 112 for 112S, 47 for S47.

## Releasing an update

1. Replace `wfa/index.html`.
2. In `wfa/sw.js`, raise the number in `VERSION` (for example `ss-wfa-v35` to `ss-wfa-v36`) and replace that file too.
3. Commit to `main`. GitHub Pages publishes within a few minutes. On phones, use **About → Check for update**.
