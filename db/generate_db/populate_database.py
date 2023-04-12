import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_events(conn):
    sql = ''' 
        INSERT INTO events (
            description
        ) 
        VALUES 
            ('Campo de Batalha'),
            ('Portão Demoníaco'),
            ('Carruagem Assombrada'),
            ('Pesadelo Ancestral'),
            ('Ofensiva'),
            ('Saquear o Cofre'),
            ('Invasão Iranata'),
            ('Guerra'),
            ('Torre da Vitória'),
            ('Assembleia das Sombras'),
            ('Rito do Exílio'),
            ('Arena Ancestral')
        ;
    '''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.lastrowid

def create_event_occurrences(conn):
    sql = ''' 
        INSERT INTO event_occurrences (event_id, occurrence_time, occurence_day_of_the_week)
    VALUES 
        (1, '08:00:00', 'Monday'),
        (1, '08:00:00', 'Tuesday'),
        (1, '08:00:00', 'Wednesday'),
        (1, '08:00:00', 'Thursday'),
        (1, '08:00:00', 'Friday'),
        (1, '08:00:00', 'Saturday'),
        (1, '08:00:00', 'Sunday'),
        (2, '12:00:00', 'Monday'),
        (3, '12:00:00', 'Tuesday'),
        (4, '12:00:00', 'Wednesday'),
        (5, '12:00:00', 'Thursday'),
        (4, '12:00:00', 'Friday'),
        (3, '12:00:00', 'Saturday'),
        (5, '12:00:00', 'Sunday'),
        (6, '12:00:00', 'Monday'),
        (6, '12:00:00', 'Tuesday'),
        (6, '12:00:00', 'Wednesday'),
        (6, '12:00:00', 'Thursday'),
        (6, '12:00:00', 'Friday'),
        (6, '12:00:00', 'Saturday'),
        (6, '12:00:00', 'Sunday'),
        (7, '12:30:00', 'Monday'),
        (7, '12:30:00', 'Tuesday'),
        (7, '12:30:00', 'Wednesday'),
        (7, '12:30:00', 'Thursday'),
        (7, '12:30:00', 'Friday'),
        (7, '12:30:00', 'Saturday'),
        (7, '12:30:00', 'Sunday'),
        (1, '12:00:00', 'Monday'),
        (1, '12:00:00', 'Tuesday'),
        (1, '12:00:00', 'Wednesday'),
        (1, '12:00:00', 'Thursday'),
        (1, '12:00:00', 'Friday'),
        (1, '12:00:00', 'Saturday'),
        (1, '12:00:00', 'Sunday'),
        (10, '19:00:00', 'Monday'),
        (10, '19:00:00', 'Tuesday'),
        (10, '19:00:00', 'Wednesday'),
        (10, '19:00:00', 'Thursday'),
        (10, '19:00:00', 'Friday'),
        (10, '19:00:00', 'Saturday'),
        (11, '20:00:00', 'Sunday'),
        (2, '20:30:00', 'Monday'),
        (3, '20:30:00', 'Tuesday'),
        (4, '20:30:00', 'Wednesday'),
        (5, '20:30:00', 'Thursday'),
        (4, '20:30:00', 'Friday'),
        (3, '20:30:00', 'Saturday'),
        (5, '20:30:00', 'Sunday'),
        (7, '21:00:00', 'Monday'),
        (7, '21:00:00', 'Tuesday'),
        (7, '21:00:00', 'Wednesday'),
        (7, '21:00:00', 'Thursday'),
        (7, '21:00:00', 'Friday'),
        (7, '21:00:00', 'Saturday'),
        (7, '21:00:00', 'Sunday'),
        (12, '21:30:00', 'Tuesday'),
        (12, '21:30:00', 'Thursday'),
        (12, '21:30:00', 'Saturday'),
        (12, '21:30:00', 'Sunday'),
        (2, '22:00:00', 'Monday'),
        (3, '22:00:00', 'Tuesday'),
        (4, '22:00:00', 'Wednesday'),
        (5, '22:00:00', 'Thursday'),
        (4, '22:00:00', 'Friday'),
        (3, '22:00:00', 'Saturday'),
        (5, '22:00:00', 'Sunday'),
        (1, '18:00:00', 'Monday'),
        (1, '18:00:00', 'Tuesday'),
        (1, '18:00:00', 'Wednesday'),
        (1, '18:00:00', 'Thursday'),
        (1, '18:00:00', 'Friday'),
        (1, '18:00:00', 'Saturday'),
        (1, '18:00:00', 'Sunday'),
        (1, '22:00:00', 'Monday'),
        (1, '22:00:00', 'Tuesday'),
        (1, '22:00:00', 'Wednesday'),
        (1, '22:00:00', 'Thursday'),
        (1, '22:00:00', 'Friday'),
        (1, '22:00:00', 'Saturday'),
        (1, '22:00:00', 'Sunday'),
        (9, '20:00:00', 'Thursday'),
        (9, '20:00:00', 'Saturday');
    '''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.lastrowid

def main():
    database = r"pythonsqlite.db"

    conn = create_connection(database)
    with conn:
        create_events(conn)
        create_event_occurrences(conn)

if __name__ == '__main__':
    main()