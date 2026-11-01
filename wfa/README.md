# Symptom Sorter (WFA)

The wilderness first aid companion to Symptom Sorter (FM-51), for IPWA patrollers. It lives in the `/wfa/` folder of this site.

**Live app:** https://mmehos77.github.io/wfa/ (the FM-51 version stays at https://mmehos77.github.io)

> Reference aid only, not a diagnosis. Follow your training, IPWA procedures and medical direction.
> The content has not been reviewed by a physician or medical director.

## What is different from the FM-51 version

- **Signs from two sources.** FM-51 (2025), quoted and checked word for word with page numbers, plus Wilderness Medical Society guideline summaries for altitude, hypothermia, frostbite, heat, hyponatremia, lightning, pit viper, anaphylaxis, spine, drowning, burns and ticks.
- **WMS wording is not checked.** It was read through a web tool that returns a processed version of each page, so each WMS sign is marked "not checked" in the app.
- **One new condition:** low blood sodium from drinking too much (exercise-associated hyponatremia), which FM-51 does not have.
- **Treatment tagged by training level** instead of EMS level: *Any first aider* (standard first aid, judged against the 2024 AHA/Red Cross first aid guidelines), *If WFA trained* (the Wilderness First Aid Scope of Practice, 2012), and *Evacuate or call for help*. Steps beyond WFA are left out. The tags are the app author's judgment.
- **Brown colour and a "WFA" icon**, so it is easy to tell apart from the green FM-51 app on a home screen.

## Files in this folder

| File | Purpose |
|---|---|
| `index.html` | The whole app, including all data |
| `sw.js` | Offline helper for this folder only (saved copies named `ss-wfa-…`) |
| `manifest.webmanifest` | App name and icons for "Add to Home Screen" |
| `icon-192.png`, `icon-512.png`, `apple-touch-icon.png` | WFA icons |

## Updating

1. Replace `index.html`.
2. In `sw.js`, raise the number in `VERSION` (for example `ss-wfa-v5` to `-v6`) and replace that file too.
3. Commit to `main`. On phones, use **About → Check for update**.
