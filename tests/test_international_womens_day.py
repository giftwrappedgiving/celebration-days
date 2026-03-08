import csv
import unittest
from pathlib import Path

DATASET_PATH = Path(__file__).resolve().parents[1] / "celebration-day.csv"


class CelebrationDatasetTests(unittest.TestCase):
    def test_international_womens_day_is_present_with_expected_fixed_date(self):
        with DATASET_PATH.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = {row["reference"]: row for row in reader}

        self.assertIn("international-womens-day", rows)
        international_womens_day = rows["international-womens-day"]
        self.assertEqual(
            international_womens_day["name"], "International Women's Day"
        )
        self.assertEqual(international_womens_day["date-type"], "fixed")
        self.assertEqual(international_womens_day["event-date"], "03-08")
        self.assertEqual(
            international_womens_day["url"],
            "https://www.unwomen.org/en/get-involved/international-womens-day",
        )


if __name__ == "__main__":
    unittest.main()
