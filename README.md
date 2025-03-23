# celebration-days

A dataset of celebration and awareness days — starting with those focused on books, reading, literacy, and libraries 📚✨

## What's in here?

This repository contains:
- `schema.md` — the data structure and field definitions.
- `celebration-day.csv` — the dataset of celebration days with key details like dates (or rules if the date isn't fixed), organisations, hashtags, and audiences.

The goal is to provide a clean, reusable dataset for anyone planning content, events, or campaigns around important days.

## Fields captured in the dataset
Each record in `celebration-day.csv` includes:
- `reference` — unique ID for the day
- `name` — name of the celebration day
- `description` — what it’s all about
- `countries` — where it’s observed
- `categories` — themes like literacy, books, libraries
- `date-type` — `fixed` or `dynamic`
- `event-date` — fixed date (if applicable, format: MM-DD)
- `date-rule` — rule for dynamic dates (e.g., "First Thursday in March")
- `first-date` — year it started
- `organisation` — who runs or recognises it
- `url` — official link
- `hashtags` — common social tags
- `audience-types` — who it’s aimed at
- `notes` — anything else useful

See `schema.md` for full definitions.

## Why does this exist?

Because we (GWG) wanted a list of celebration days

This dataset might help:
✅ Content planners  
✅ Educators and librarians  
✅ Campaigners  
✅ Curious data nerds  

## Contributing

Spotted a missing day or a mistake? PRs welcome!
- Add new rows to `celebration-day.csv`
- Stick to the existing format (check `schema.md`)
- Bonus points for sourcing the official URL 🎯

## Ideas / TODOs
- Expand beyond books and literacy? (Health, environment, arts…)
- Add iCal / JSON export
- Auto-calculate dynamic dates per year?

## Licence
MIT — do what you like, just don’t blame us if you turn up to *World Book Day* in fancy dress on the wrong day.

---

Pull requests, ideas, and celebration day suggestions always welcome 🎉
