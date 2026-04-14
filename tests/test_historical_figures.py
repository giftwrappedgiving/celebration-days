import csv
import unittest
from pathlib import Path


DATASET_PATH = Path(__file__).resolve().parents[1] / "data" / "historical-figure.csv"


class HistoricalFigureDatasetTests(unittest.TestCase):
    def test_seed_figures_are_present(self):
        with DATASET_PATH.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = {row["reference"]: row for row in reader}

        self.assertIn("nelson-mandela", rows)
        self.assertIn("bob-marley", rows)

        self.assertEqual(
            rows["nelson-mandela"]["wikipedia-url"],
            "https://en.wikipedia.org/wiki/Nelson_Mandela",
        )
        self.assertEqual(
            rows["bob-marley"]["wikipedia-url"],
            "https://en.wikipedia.org/wiki/Bob_Marley",
        )


if __name__ == "__main__":
    unittest.main()
