import csv
import unittest
from pathlib import Path


DATASET_PATH = Path(__file__).resolve().parents[1] / "celebration-day.csv"


class CelebrationDatasetTests(unittest.TestCase):
    def test_world_afro_day_is_present_with_expected_fixed_date(self):
        with DATASET_PATH.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = {row["reference"]: row for row in reader}

        self.assertIn("world-afro-day", rows)

        world_afro_day = rows["world-afro-day"]
        self.assertEqual(world_afro_day["name"], "World Afro Day")
        self.assertEqual(world_afro_day["date-type"], "fixed")
        self.assertEqual(world_afro_day["event-date"], "09-15")
        self.assertEqual(world_afro_day["url"], "https://www.worldafroday.com/")

    def test_world_environment_day_is_present_with_expected_fixed_date(self):
        with DATASET_PATH.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = {row["reference"]: row for row in reader}

        self.assertIn("world-environment-day", rows)

        world_environment_day = rows["world-environment-day"]
        self.assertEqual(world_environment_day["name"], "World Environment Day")
        self.assertEqual(world_environment_day["date-type"], "fixed")
        self.assertEqual(world_environment_day["event-date"], "06-05")
        self.assertEqual(
            world_environment_day["url"],
            "https://www.unep.org/events/un-day/world-environment-day",
        )

if __name__ == "__main__":
    unittest.main()
