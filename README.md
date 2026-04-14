# celebration-days

A dataset project for celebration/awareness days and notable historical figures.

## Repository structure

```text
.
├── data/
│   ├── celebration-day.csv
│   └── historical-figure.csv
├── schema/
│   ├── celebration-day.schema.md
│   └── historical-figure.schema.md
├── python/
│   ├── pyproject.toml
│   ├── README.md
│   └── src/celebration_days/
├── requirements/
├── tests/
├── Makefile
└── README.md
```

## Datasets

- `data/celebration-day.csv`: celebration and awareness days.
- `data/historical-figure.csv`: historically significant people with birthdays and Wikipedia URLs.

## Schemas

- `schema/celebration-day.schema.md`
- `schema/historical-figure.schema.md`

## Python package

Python interfaces live in `python/src/celebration_days`.

Quick start:

```bash
cd python
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m celebration_days.main
```

## Development

Install shared dev dependencies and run tests:

```bash
make init
make tests
```

Current tests validate the canonical dataset files in `data/`.
