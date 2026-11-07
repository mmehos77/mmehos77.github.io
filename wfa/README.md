# Symptom Sorter (WFA)

An offline wilderness first aid reference for Indian Peaks Wilderness Alliance (IPWA) patrollers. You enter the signs you find, and it lists the conditions that best match, with first aid steps tagged by training level.

**Live app:** https://mmehos77.github.io/wfa/

> Reference aid only, not a diagnosis. Follow your training, IPWA procedures and medical direction.
> The content has not been reviewed by a physician or medical director.

This is the only maintained version. The FM-51-only version that used to be at https://mmehos77.github.io was retired in November 2026; that address now forwards here.

## What it covers

- **61 conditions:** the conditions in NPS / USFS Field Manual #51 (2025), plus low blood sodium from drinking too much (exercise-associated hyponatremia), which FM-51 does not have.
- **Signs from two kinds of sources.** Each sign on a condition's page names its source:
  - **FM-51 (2025):** quoted word for word with page numbers. Some links are marked as an item FM-51 says to check, or as the app's reading of FM-51 text.
  - **Full Wilderness Medical Society (WMS) guidelines:** heat illness 2024, altitude 2024, hypothermia 2019, frostbite 2024, spine 2024 and burns 2025. Quoted word for word, with the printed page (for example "WMS Heat Illness 2024 p.114S").
  - **WMS guideline summaries:** anaphylaxis, pit viper, lightning, drowning, hyponatremia and ticks, plus one hypothermia sign. These were read through a web tool and are marked "not checked" in the app.
- **Rules from the sources:**
  - Some signs make a condition less likely. For example, frostbite in rain, because frostbite needs tissue to freeze (WMS Frostbite 2024 p.185); and heat cramps with no cramps entered.
  - Some sign combinations raise urgency.
  - The burn card notes that confusion is not expected from a burn itself.
- **Treatment tagged by training level:**
  - *Any first aider* (standard first aid, judged against the AHA / Red Cross first aid guidelines 2020 and 2024, and AHA 2025 Adult Basic Life Support for CPR);
  - *If WFA trained* (the Wilderness First Aid Scope of Practice, 2012);
  - *Evacuate or call for help*.

  Steps beyond WFA training are left out, for example a bag-valve mask, oral airway and IV fluids. The tags are the app author's judgment.
- **Typed notes are read too.** Free text such as a SOAP note or radio report suggests signs, including vital signs (pulse, breathing, temperature, blood sugar, A&O ×4, AVPU) and denials ("denies chest pain").
- **A note when only one or two signs are entered,** saying the list is a rough guide until more signs are added.
- **Brown colour and a "WFA" icon** on the home screen.

## Files in this folder

| File | Purpose |
|---|---|
| `index.html` | The whole app, including all data |
| `sw.js` | Offline helper for this folder only (saved copies named `ss-wfa-…`) |
| `manifest.webmanifest` | App name and icons for "Add to Home Screen" |
| `icon-192.png`, `icon-512.png`, `apple-touch-icon.png` | WFA icons |

## Checking citations

From the top of the repository, with the PDFs on your own computer (they are not kept in the repository):

```
python3 tools/check_citations.py FM51.pdf wfa/index.html
python3 tools/check_wms.py wfa/index.html heat24=heat.pdf:112 alt24=alt.pdf:2 hypo19=hypo.pdf:47 fb24=fb.pdf:183 spine24=spine.pdf:78 burn25=burns.pdf:549
```

Both print `OK` when every quote is found on its cited page.

## Updating

1. Replace `index.html`.
2. In `sw.js`, raise the number in `VERSION` (for example `ss-wfa-v35` to `ss-wfa-v36`) and replace that file too.
3. Commit to `main`. On phones, use **About → Check for update**.
