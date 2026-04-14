from datetime import datetime
from pathlib import Path
from typing import Optional, Union

import pandas as pd


class HistoricalFigureInterface:
    def __init__(self, csv_file: Union[str, Path]):
        self.csv_file = Path(csv_file)
        self.data = self.load_data()

    def load_data(self):
        return pd.read_csv(self.csv_file)

    def get_figure_by_name(self, name: str) -> Optional[str]:
        figure = self.data[self.data["name"].str.lower() == name.lower()]
        if not figure.empty:
            return figure.iloc[0].to_json()
        return None

    def get_next_birthday(self) -> Optional[str]:
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        self.data["birth-date"] = self.data["birth-date"].apply(
            lambda x: self.parse_date(x) if pd.notnull(x) and str(x).strip() else None
        )
        upcoming = self.data[self.data["birth-date"] > today].sort_values("birth-date")
        if not upcoming.empty:
            return upcoming.iloc[0].to_json()
        return None

    def parse_date(self, date_str: str) -> Optional[datetime]:
        if "-" in date_str:
            return datetime.strptime(date_str, "%m-%d").replace(year=datetime.now().year)
        return None
