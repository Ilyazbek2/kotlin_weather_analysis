from src.lucky_days import get_number_of_lucky_days
import sqlite3

def test_empty_table(tmp_path):
    db = tmp_path / "test.db"
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("CREATE TABLE table_green_future (date TEXT, activity TEXT)")
    result = get_number_of_lucky_days(cur, 1)
    assert result == 0.0
