# Python Interfaces

This folder contains lightweight Python interfaces for the datasets in the repository-level `data/` directory.

## Run locally

```bash
cd python
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m celebration_days.main
```

## Available interfaces

- `celebration_days.CelebrationInterface`
- `celebration_days.HistoricalFigureInterface`
