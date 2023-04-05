import sqlite3
from sqlite3 import Error

database = r"pythonsqlite.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def find_events_by_time_and_day_of_the_week(time, day):
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT DISTINCT events.description FROM events AS events INNER JOIN event_occurrences AS eo ON eo.event_id = events.id WHERE eo.occurrence_time == ? AND eo.occurence_day_of_the_week == ? ;", (time, day, ))

    rows = cur.fetchall()

    conn.close()

    return rows

def find_event_by_id(id):
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT DISTINCT events.description FROM events where id = ?;", (id, ))

    rows = cur.fetchall()

    conn.close()

    return rows