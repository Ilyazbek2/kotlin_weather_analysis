import sqlite3

def count_hurricane_days(cursor: sqlite3.Cursor) -> int:
    """
    Count days with wind >= 33 m/s.
    """
    cursor.execute("SELECT COUNT(*) FROM table_kotlin WHERE wind >= 33")
    (count,) = cursor.fetchone()
    return count
