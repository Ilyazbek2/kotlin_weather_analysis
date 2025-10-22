from src.db_utils import get_connection
from src.hurricane_analysis import count_hurricane_days
from src.lucky_days import get_number_of_lucky_days

def main():
    with get_connection() as conn:
        c = conn.cursor()
        hurricanes = count_hurricane_days(c)
        print(f"🌪 Total hurricane days over Kotlin: {hurricanes}")

        lucky_percent = get_number_of_lucky_days(c, 12)
        print(f"🍀 Lucky days in December: {lucky_percent:.2f}%")

if __name__ == "__main__":
    main()
