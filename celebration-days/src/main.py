from celebration_interface import CelebrationInterface
from datetime import date

# Path to your CSV file
CSV_PATH = "../../celebration-day.csv"

# Create the interface
celebrations = CelebrationInterface(CSV_PATH)

# Get the next celebration day from today
next_celebration = celebrations.get_next_celebration_day()

print("Next celebration day:")
print(next_celebration)