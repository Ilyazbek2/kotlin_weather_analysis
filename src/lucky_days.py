from collections import defaultdict
import sqlite3

def get_number_of_lucky_days(cursor: sqlite3.Cursor, month: int) -> float:
    """
    Calculate the percentage of 'lucky' days in a given month.
    """
    cursor.execute(
        "SELECT date, activity FROM table_green_future WHERE strftime('%m', date)=?",
        (f"{month:02}",)
    )
    days = defaultdict(list)
    for d, a in cursor.fetchall():
        days[d].append(a)

    lucky = sum(
        acts.count("мешок пластика") >= 2 and
        acts.count("мешок алюминия") >= 1 and
        "отнесли мешки на завод" in acts
        for acts in days.values()
    )
    return 0 if not days else lucky / len(days) * 100
