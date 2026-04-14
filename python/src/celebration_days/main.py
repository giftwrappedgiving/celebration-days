from pathlib import Path

from celebration_days.celebration_interface import CelebrationInterface


def main():
    data_path = Path(__file__).resolve().parents[3] / "data" / "celebration-day.csv"
    celebrations = CelebrationInterface(data_path)
    next_celebration = celebrations.get_next_celebration_day()

    print("Next celebration day:")
    print(next_celebration)


if __name__ == "__main__":
    main()
