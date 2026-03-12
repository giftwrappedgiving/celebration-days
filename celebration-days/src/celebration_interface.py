import pandas as pd
from datetime import datetime


class CelebrationInterface:
    
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = self.load_data()

    def load_data(self):
        return pd.read_csv(self.csv_file)

    def get_next_celebration_day(self):
        today = datetime.now().strftime('%m-%d')
        self.data['event-date'] = self.data['event-date'].apply(
            lambda x: self.parse_date(x) if pd.notnull(x) and x.strip() else None
        )
        upcoming = self.data[self.data['event-date'] > today].sort_values('event-date')
        if not upcoming.empty:
            return upcoming.iloc[0].to_json()
        return None

    def get_celebration_by_name(self, name):
        celebration = self.data[self.data['name'].str.lower() == name.lower()]
        if not celebration.empty:
            return celebration.iloc[0].to_json()
        return None

    def parse_date(self, date_str):
        """
        Parse a date string from the CSV and return a datetime object for this year.
        Example:
            parse_date('04-23') -> datetime object for April 23 this year
            parse_date('')      -> None (for dynamic or missing dates)
        """
        print(f"Parsing date: {date_str}")
        if '-' in date_str:
            # Example: '04-23' becomes datetime(year, 4, 23)
            return datetime.strptime(date_str, '%m-%d').replace(year=datetime.now().year)
        # Handle dynamic dates based on rules if necessary
        return None