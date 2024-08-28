import sqlite3

def create_table():
    conn = sqlite3.connect('project_database.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys = ON;')

    # Create user table
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS user(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            password VARCHAR(256),
            user_type BOOLEAN,
            name VARCHAR(256),
            phone_number INT,
            email_address VARCHAR(256),
            gender VARCHAR(10),
            age YEAR 
        ); 
    ''')

    # Create ticket table without ticket_type
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS ticket(
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            schedule_id INTEGER REFERENCES event_schedule (schedule_id),
            price FLOAT 
        ); 
    ''')

    # Other tables remain unchanged
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS ticket_sales(
            sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES user (user_id),
            ticket_id INTEGER REFERENCES ticket (ticket_id),
            sale_time DATETIME 
        ); 
    ''')

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS event(
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            venue_id INTEGER REFERENCES venue (venue_id) ON DELETE CASCADE,
            event_name VARCHAR(256),
            event_description TEXT,
            created_at DATETIME 
        ); 
    ''')

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS event_schedule(
            schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER REFERENCES event (event_id) ON DELETE CASCADE,
            schedule_name VARCHAR(256),
            schedule_start_time DATETIME,
            schedule_end_time DATETIME,
            schedule_description TEXT 
        ); 
    ''')

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS venue(
            venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location VARCHAR(256),
            capacity INT 
        ); 
    ''')

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS feedback(
            feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER REFERENCES ticket (ticket_id) ON DELETE CASCADE,
            comment TEXT,
            ratings FLOAT 
        ); 
    ''')

    conn.commit()
    conn.close()