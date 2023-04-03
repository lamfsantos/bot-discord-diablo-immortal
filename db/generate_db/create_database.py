import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"pythonsqlite.db"

    sql_create_event_table = """ CREATE TABLE IF NOT EXISTS events (
                                        id integer PRIMARY KEY,
                                        description text NOT NULL
                                    ); """

    sql_create_event_occurrences_table = """CREATE TABLE IF NOT EXISTS event_occurrences  (
                                    id integer PRIMARY KEY,
                                    event_id INTEGER NOT NULL,
                                    occurrence_time TIME NOT NULL,
                                    occurence_day_of_the_week text NOT NULL,
                                    FOREIGN KEY (event_id) REFERENCES events(id)
                                );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_event_table)

        create_table(conn, sql_create_event_occurrences_table)
    else:
        print("Erro! não foi possivel criar a conexão com o bd.")

if __name__ == '__main__':
    main()