from datetime import datetime
from pathlib import Path
from typing import Optional, Union

import pandas as pd


class CelebrationInterface:
    def __init__(self, csv_file: Union[str, Path]):
        self.csv_file = Path(csv_file)
        self.data = self.load_data()

    def load_data(self):
        return pd.read_csv(self.csv_file)

    def get_next_celebration_day(self) -> Optional[str]:
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        self.data["event-date"] = self.data["event-date"].apply(
            lambda x: self.parse_date(x) if pd.notnull(x) and x.strip() else None
        )
        upcoming = self.data[self.data["event-date"] > today].sort_values("event-date")
        if not upcoming.empty:
            return upcoming.iloc[0].to_json()
        return None

    def get_celebration_by_name(self, name: str) -> Optional[str]:
        celebration = self.data[self.data["name"].str.lower() == name.lower()]
        if not celebration.empty:
            return celebration.iloc[0].to_json()
        return None

    def parse_date(self, date_str: str) -> Optional[datetime]:
        if "-" in date_str:
            return datetime.strptime(date_str, "%m-%d").replace(year=datetime.now().year)
        return None
