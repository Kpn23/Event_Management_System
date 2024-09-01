import sqlite3
import csv
from datetime import datetime


def create_table():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Create user table
    cursor.execute(
        """ 
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
    """
    )

    # Create ticket table without ticket_type
    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS ticket(
            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
            schedule_id INTEGER REFERENCES event_schedule (schedule_id),
            price FLOAT 
        ); 
    """
    )

    # Other tables remain unchanged
    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS ticket_sales(
            sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES user (user_id),
            ticket_id INTEGER REFERENCES ticket (ticket_id),
            sale_time DATETIME 
        ); 
    """
    )

    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS event(
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            venue_id INTEGER REFERENCES venue (venue_id) ON DELETE CASCADE,
            event_name VARCHAR(256),
            event_description TEXT,
            created_at DATETIME 
        ); 
    """
    )

    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS event_schedule(
            schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER REFERENCES event (event_id) ON DELETE CASCADE,
            schedule_name VARCHAR(256),
            schedule_start_time DATETIME,
            schedule_end_time DATETIME,
            schedule_description TEXT 
        ); 
    """
    )

    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS venue(
            venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location VARCHAR(256),
            capacity INT 
        ); 
    """
    )

    cursor.execute(
        """ 
        CREATE TABLE IF NOT EXISTS feedback(
            feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER REFERENCES ticket (ticket_id) ON DELETE CASCADE,
            comment TEXT,
            ratings FLOAT 
        ); 
    """
    )

    conn.commit()
    conn.close()


#######################################################################^^^^^^^^CREATE TABLE FUNCTION^^^^^^^^^#########################################################################################################################################################
def add_user(password, user_type, name, phone, email, gender, age):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user (password, user_type, name, phone_number, email_address, gender, age) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (password, user_type, name, phone, email, gender, age),
    )
    conn.commit()
    conn.close()
    print(f"User {name} added successfully.")


def add_ticket(schedule_id, price):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ticket (schedule_id, price) VALUES (?, ?)", (schedule_id, price)
    )
    conn.commit()
    conn.close()
    print("Ticket added successfully.")


def add_ticket_sales(user_id, ticket_id, sale_time):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ticket_sales (user_id, ticket_id, sale_time) VALUES (?, ?, ?)",
        (user_id, ticket_id, sale_time),
    )
    conn.commit()
    conn.close()
    print("Ticket sale added successfully.")


def add_event(venue_id, event_name, event_description):
    created_at = datetime.now()
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO event (venue_id, event_name, event_description, created_at) VALUES (?, ?, ?, ?)",
        (venue_id, event_name, event_description, created_at),
    )
    conn.commit()
    conn.close()
    print("Event added successfully.")


def add_event_schedule(
    event_id,
    schedule_name,
    schedule_start_time,
    schedule_end_time,
    schedule_description,
):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO event_schedule (event_id, schedule_name, schedule_start_time, schedule_end_time, schedule_description) VALUES (?, ?, ?, ?, ?)",
        (
            event_id,
            schedule_name,
            schedule_start_time,
            schedule_end_time,
            schedule_description,
        ),
    )
    conn.commit()
    conn.close()
    print("Event schedule added successfully.")


def add_venue(location, capacity):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO venue (location, capacity) VALUES (?, ?)", (location, capacity)
    )
    conn.commit()
    conn.close()
    print("Venue added successfully.")


def add_feedback(ticket_id, comment, ratings):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO feedback (ticket_id, comment, ratings) VALUES (?, ?, ?)",
        (ticket_id, comment, ratings),
    )
    conn.commit()
    conn.close()
    print("Feedback added successfully.")


############################################################################^^^^ADD FUNCTION^^^^^^^^^###########################################################################################################################################################
import sqlite3


def view_user():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(
                f"user_id: {row[0]}, password: {row[1]}, user_type: {row[2]}, name: {row[3]}, phone_number: {row[4]}, email_address: {row[5]}, gender: {row[6]}, age: {row[7]}"
            )
    else:
        print("No user found.")


def view_tickets():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ticket")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"ticket_id: {row[0]}, schedule_id: {row[1]}, price: {row[2]}")
    else:
        print("No ticket found.")


def view_ticket_sales():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ticket_sales")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(
                f"sales_id: {row[0]}, user_id: {row[1]}, ticket_id: {row[2]}, sale_time: {row[3]}"
            )
    else:
        print("No ticket sales found.")


def view_event():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM event AS e
        JOIN venue AS v USING(venue_id)
    """
    )
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(
                f"event_id: {row[0]}, venue_id: {row[1]}, event_name: {row[2]}, event_description: {row[3]}, created_at: {row[4]}, location: {row[5]}, capacity:{row[6]}"
            )
    else:
        print("No event found.")


def view_event_schedule():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT *
        FROM event_schedule
    """
    )
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(
                f"schedule_id: {row[0]}, event_id: {row[1]}, schedule_name: {row[2]}, schedule_start_time: {row[3]}, schedule_end_time: {row[4]}, schedule_description: {row[5]}"
            )
    else:
        print("No event schedule found.")


def view_venue():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM venue")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"venue_id: {row[0]}, location: {row[1]}, capacity: {row[2]}")
    else:
        print("No venue found.")


def view_feedback():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT f.feedback_id, f.ticket_id, f.comment, f.ratings, e.event_name 
        FROM feedback f 
        JOIN ticket t ON f.ticket_id = t.ticket_id 
        JOIN event_schedule es ON t.schedule_id = es.schedule_id 
        JOIN event e ON es.event_id = e.event_id
        ORDER BY event_name
    """
    )
    rows = cursor.fetchall()
    conn.close()

    if rows:
        for row in rows:
            print(
                f"event_name: {row[4]},feedback_id: {row[0]}, ticket_id: {row[1]}, comment: {row[2]}, ratings: {row[3]}"
            )
    else:
        print("No feedback found.")


############################################################################^^^^VIEW FUNCTION^^^^^^^^^################################################################################################################################################
def update_user(
    user_id,
    new_password,
    new_user_type,
    new_name,
    new_phone,
    new_email,
    new_gender,
    new_age,
):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE user 
        SET password = ?, user_type = ?, name = ?, phone_number = ?, email_address = ?, gender = ?, age = ?
        WHERE user_id = ?;
    """,
        (
            new_password,
            new_user_type,
            new_name,
            new_phone,
            new_email,
            new_gender,
            new_age,
            user_id,
        ),
    )
    conn.commit()
    conn.close()
    print("User information updated successfully.")


def update_ticket(ticket_id, new_schedule_id, new_price):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """ 
        UPDATE ticket SET schedule_id = ?, price = ? WHERE ticket_id = ?; 
    """,
        (new_schedule_id, new_price, ticket_id),
    )
    conn.commit()
    conn.close()
    print("Ticket information updated successfully.")


def update_ticket_sales(sales_id, new_user_id, new_ticket_id, new_sale_time):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE ticket_sales 
        SET user_id = ?, ticket_id = ?, sale_time = ?
        WHERE sales_id = ?;
    """,
        (new_user_id, new_ticket_id, new_sale_time, sales_id),
    )
    conn.commit()
    conn.close()
    print("Ticket sales information updated successfully.")


def update_event(event_id, new_venue_id, new_event_name, new_event_description):
    new_created_at = datetime.now()
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE event 
        SET venue_id = ?, event_name = ?, event_description = ?, created_at = ?
        WHERE event_id = ?;
    """,
        (new_venue_id, new_event_name, new_event_description, new_created_at, event_id),
    )
    conn.commit()
    conn.close()
    print("Event information updated successfully.")


def update_event_schedule(
    schedule_id,
    new_event_id,
    new_schedule_name,
    new_start_time,
    new_end_time,
    new_description,
):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE event_schedule 
        SET event_id = ?, schedule_name = ?, schedule_start_time = ?, schedule_end_time = ?, schedule_description = ?
        WHERE schedule_id = ?;
    """,
        (
            new_event_id,
            new_schedule_name,
            new_start_time,
            new_end_time,
            new_description,
            schedule_id,
        ),
    )
    conn.commit()
    conn.close()
    print("Event schedule information updated successfully.")


def update_venue(venue_id, new_location, new_capacity):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE venue 
        SET location = ?, capacity = ?
        WHERE venue_id = ?;
    """,
        (new_location, new_capacity, venue_id),
    )
    conn.commit()
    conn.close()
    print("Venue information updated successfully.")


def update_feedback(feedback_id, new_ticket_id, new_comment, new_ratings):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE feedback 
        SET ticket_id = ?, comment = ?, ratings = ?
        WHERE feedback_id = ?;
    """,
        (new_ticket_id, new_comment, new_ratings, feedback_id),
    )
    conn.commit()
    conn.close()
    print("Feedback information updated successfully.")


###########################################################################^^^^^^^ EDIT ^^^^^^^^^################################################################################################################
import sqlite3


def del_user(user_id):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("User deleted successfully.")


def del_ticket(ticket_id):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ticket WHERE ticket_id = ?", (ticket_id,))
    conn.commit()
    conn.close()
    print("Ticket deleted successfully.")


def del_ticket_sale(sales_id):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("DELETE FROM ticket_sales WHERE sales_id = ?", (sales_id,))
    conn.commit()
    conn.close()
    print("Ticket sale deleted successfully.")


def del_event(event_id):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("DELETE FROM event WHERE event_id = ?", (event_id,))
    conn.commit()
    conn.close()
    print("Event deleted successfully.")


"""
def del_venue(venue_id):
    conn = sqlite3.connect('project_database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM venue WHERE venue_id = ?', (venue_id,))
    conn.commit()
    conn.close()
    print("Venue deleted successfully.")
"""


def del_feedback(feedback_id):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("DELETE FROM feedback WHERE feedback_id = ?", (feedback_id,))
    conn.commit()
    conn.close()
    print("Feedback deleted successfully.")


###########################################################################^^^^^^^ DELETE ^^^^^^^^^################################################################################################################


def admin_reporting_and_analytics():
    while True:
        print("\nReporting and Analytics Menu:")
        print("1. Search Records")
        print("2. Generate Reports")
        print("3. Analyze Data")
        print("4. Export Data to CSV")
        print("5. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            search_records()
        elif choice == 2:
            generate_reports()
        elif choice == 3:
            analyze_data()
        elif choice == 4:
            export_data_to_csv()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


def search_records():
    criteria = input("Enter search criteria (e.g., user name, event name): ")
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM user WHERE name LIKE ? OR email_address LIKE ?",
        ("%" + criteria + "%", "%" + criteria + "%"),
    )
    results = cursor.fetchall()
    conn.close()

    if results:
        for row in results:
            print(row)
    else:
        print("No records found.")


def generate_reports():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()

    # Example: Generate sales report
    cursor.execute(
        "SELECT e.event_name, COUNT(ts.ticket_id) AS total_sales FROM ticket_sales ts JOIN ticket t ON ts.ticket_id = t.ticket_id JOIN event_schedule es ON t.schedule_id = es.schedule_id JOIN event e ON es.event_id = e.event_id GROUP BY e.event_name"
    )
    sales_report = cursor.fetchall()

    print("Sales Report:")
    for row in sales_report:
        print(f"Event: {row[0]}, Total Sales: {row[1]}")

    conn.close()


def analyze_data():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()

    # Example: Analyze user activity
    cursor.execute(
        "SELECT user_id, COUNT(ticket_id) AS tickets_purchased FROM ticket_sales GROUP BY user_id"
    )
    user_activity = cursor.fetchall()

    print("User Activity Analysis:")
    for row in user_activity:
        print(f"User ID: {row[0]}, Tickets Purchased: {row[1]}")

    conn.close()


def export_data_to_csv():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ticket_sales")
    rows = cursor.fetchall()

    with open(
        "/Users/superdayuanjingzhi/Downloads/ticket_sales_report.csv", "w", newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["Sales ID", "User ID", "Ticket ID", "Sale Time"])
        writer.writerows(rows)

    print("Data exported to ticket_sales_report.csv successfully.")
    conn.close()


############################################################################^^^^ Analyse Report^^^^^^^^^###########################################################################################################################


def admin_choose_function():
    print("")
    print("\nWelcome to the Event Management System! Please select a table to edit: ")
    print("1. Manage user")
    print("2. Manage event")
    print("3. Manage venue")
    print("4. Manage Ticket")
    print("5. Manage Feedback")
    print("6. Analyse report")
    print("7. EXIT THE SYSTEM")


def admin_user_management():
    print("")
    print("\nThis is the User Management section. Would you like to:")
    print("1. View user")
    print("2. Add user")
    print("3. Edit user")
    print("4. Delete user")
    print("5. Return to main menu")


def admin_event_management():
    print("")
    print("\nThis is the Event Management section. Would you like to:")
    print("1. View event")
    print("2. Add event")
    print("3. Edit event")
    print("4. Edit event schedule")
    print("5. Delete event")
    print("6. Return to main menu")


def admin_venue_management():
    print("")
    print("\nThis is the Venue Management section. Would you like to:")
    print("1. View venue")
    print("2. Add venue")
    print("3. Edit venue")
    # print("4. Delete venue")
    print("4. Return to main menu")


def admin_ticket_management():
    print("")
    print("\nThis is the Ticket Management section. Would you like to:")
    print("1. View ticket")
    print("2. Add ticket")
    print("3. Edit ticket")
    print("4. Delete ticket")
    print("5. Return to main menu")


def admin_feedback_management():
    print("")
    print("\nThis is the Feedback Management section. Would you like to:")
    print("1. View feedback")
    print("2. Add feedback")
    print("3. Edit feedback")
    print("4. Delete feedback")
    print("5. Return to main menu")


############################################################################^^^^ USER FUNCTION OPTIONS^^^^^^^^^###########################################################################################################################
def user_choose_function():
    print("")
    print("\nWelcome to the Event Management System! Please select a table to edit: ")
    print("1. Manage account")
    print("2. Manage event")
    print("3. Manage Ticket")
    print("4. Manage Feedback")
    print("5. EXIT THE SYSTEM")


def user_notification():
    print("1. View feedback")
    print("2. Add feedback")
    print("3. Edit feedback")
    print("4. Delete feedback")
    print("5. Return to main menu")


############################################################################^^^^ USER FUNCTION OPTIONS^^^^^^^^^###########################################################################################################################
def authenticate_user(name, password):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()

    # Retrieve record from 'user' table
    cursor.execute("SELECT * FROM user WHERE name = ?", (name,))
    user_record = cursor.fetchone()

    if user_record is None:
        print("Account does not exist.")
        return None  # Return None if the account does not exist
    else:
        stored_password = user_record[1]  # Assuming password is the second column
        user_type = user_record[2]  # Assuming user_type is the third column

        if stored_password == password:
            print(f"Authentication successful.")
            return user_type  # Return user_type if authentication is successful
        else:
            print("Incorrect password.")
            return None  # Return None if the password is incorrect
    conn.close()


###################################################################################


def view_PA(name, password):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    # Retrieve record from 'user' table
    cursor.execute(
        "SELECT * FROM user WHERE name = ? and password =?", (name, password)
    )
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(
                f"user_id: {row[0]}, password: {row[1]}, user_type: {row[2]}, name: {row[3]}, phone_number: {row[4]}, email_address: {row[5]}, gender: {row[6]}, age: {row[7]}"
            )
    else:
        print("No user found.")


def edit_PA(
    name,
    password,
    new_user_name,
    new_user_password,
    new_user_pn,
    new_user_email,
    new_user_gender,
    new_user_age,
):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    # Retrieve record from 'user' table
    cursor.execute(
        """UPDATE user
                   SET name = ?, password = ?, phone_number = ?, email_address = ?,gender = ?, age = ?
                   WHERE name = ? and password = ? """,
        (
            new_user_name,
            new_user_password,
            new_user_pn,
            new_user_email,
            new_user_gender,
            new_user_age,
            name,
            password,
        ),
    )
    conn.commit()
    conn.close()
    print("User information updated successfully.")


def user_view_event():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute(
        """SELECT e.event_id,e.event_name, e.event_description, es.schedule_id,es.schedule_name,
                   es.schedule_start_time, es.schedule_end_time, es.schedule_description,v.venue_id,v.location,v.capacity
                   FROM event e
                   JOIN event_schedule es
                   USING (event_id)
                   JOIN venue v
                   ON e.venue_id = v.venue_id"""
    )
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(
                f"event_id: {row[0]}, event_name: {row[1]}, event_description: {row[2]},\nschedule_id: {row[3]}, "
                f"schedule_name: {row[4]}, schedule_start_time: {row[5]}, schedule_end_time: {row[6]}, "
                f"schedule_description: {row[7]},\nvenue_id: {row[8]}, location: {row[9]}, capacity: {row[10]}"
            )
    else:
        print("No result found.")


def user_view_feedback():
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"comment: {row[2]}, ratings: {row[3]}")
    else:
        print("No feedback found.")


####################################################################################


def choose_admin_user_management(function_choice):
    admin_user_management()
    function_choice = int(input("Choose your option: "))
    return function_choice


##################################^^^^^^Page^^^^^^##############################################


def check_tickets(login_user_id):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()

    # View events
    cursor.execute("SELECT event_id, event_name FROM event")
    events = cursor.fetchall()

    if not events:
        print("No events available.")
        return

    print("Available Events:")
    for idx, (event_id, event_name) in enumerate(events):
        print(f"{idx + 1}. {event_name} (ID: {event_id})")

    # User selects an event
    event_choice = int(input("Choose an event by number: ")) - 1
    selected_event = events[event_choice][0]

    # View event schedules and ticket prices
    cursor.execute(
        """
        SELECT es.schedule_id, es.schedule_name, t.ticket_id, t.price, v.capacity - COUNT(ts.ticket_id) as remaining_capacity
        FROM event_schedule es
        JOIN ticket t ON es.schedule_id = t.schedule_id
        LEFT JOIN ticket_sales ts ON t.ticket_id = ts.ticket_id
        JOIN venue v ON es.event_id = v.venue_id
        WHERE es.event_id = ?
        GROUP BY es.schedule_id
    """,
        (selected_event,),
    )

    schedules = cursor.fetchall()

    if not schedules:
        print("No schedules available for this event.")
        return

    print("Available Schedules and Prices:")
    for idx, (
        schedule_id,
        schedule_name,
        ticket_id,
        price,
        remaining_capacity,
    ) in enumerate(schedules):
        print(
            f"{idx + 1}. Schedule: {schedule_name}, Price: {price}, Remaining: {remaining_capacity}"
        )

    # User selects a schedule
    schedule_choice = int(input("Choose a schedule by number: ")) - 1
    selected_schedule = schedules[schedule_choice]

    if selected_schedule[4] == 0:  # Adjusted index for remaining_capacity
        print(
            "Selected schedule has no remaining capacity. Please choose another schedule."
        )
        return

    # Reserve Tickets using schedule_id and ticket_id
    reserve_tickets(
        selected_schedule[0], selected_schedule[2], login_user_id
    )  # Use schedule_id and ticket_id here

    conn.close()


def reserve_tickets(schedule_id, ticket_id, login_user_id):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()

    # Check if the user has already reserved this ticket
    cursor.execute(
        """
        SELECT COUNT(*) FROM ticket_sales
        WHERE user_id = ? AND ticket_id = ?
    """,
        (login_user_id, ticket_id),
    )

    already_reserved = cursor.fetchone()[0]

    if already_reserved > 0:
        print(
            "You have already reserved this ticket. You can only reserve one ticket of the same type at a time."
        )
        conn.close()
        return

    sale_time = datetime.now()

    # Insert ticket sale
    cursor.execute(
        """
        INSERT INTO ticket_sales (user_id, ticket_id, sale_time)
        VALUES (?, ?, ?)
    """,
        (login_user_id, ticket_id, sale_time),
    )  # Use ticket_id in the query

    print(f"Successfully reserved 1 ticket.")

    conn.commit()
    conn.close()


def view_purchased_tickets(login_user_id):
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT t.ticket_id, e.event_name, ts.sale_time
        FROM ticket_sales ts
        JOIN ticket t ON ts.ticket_id = t.ticket_id
        JOIN event e ON t.schedule_id = e.event_id
        WHERE ts.user_id = ?
    """,
        (login_user_id,),
    )

    purchased_tickets = cursor.fetchall()

    if not purchased_tickets:
        print("No purchased tickets found.")
    else:
        print("Purchased Tickets:")
        for ticket in purchased_tickets:
            print(f"Ticket ID: {ticket[0]}, Event: {ticket[1]}, Sale Time: {ticket[2]}")

    conn.close()


def cancel_tickets(login_user_id):
    ticket_id = int(input("Enter the ticket ID to cancel: "))
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()

    # Check if the ticket belongs to the user
    cursor.execute(
        """ SELECT COUNT(*) FROM ticket_sales WHERE ticket_id = ? AND user_id = ? """,
        (ticket_id, login_user_id),
    )
    if cursor.fetchone()[0] == 0:
        print("Ticket not found or does not belong to you.")
        return

    # Find the schedule_id associated with the ticket
    cursor.execute(
        """ SELECT schedule_id FROM ticket WHERE ticket_id = ? """, (ticket_id,)
    )
    schedule_id = cursor.fetchone()[0]

    # Delete the ticket sale
    cursor.execute(
        "DELETE FROM ticket_sales WHERE ticket_id = ? AND user_id = ?",
        (ticket_id, login_user_id),
    )
    print("Ticket canceled successfully.")

    # Calculate remaining capacity
    cursor.execute(
        """
        SELECT v.capacity - COUNT(ts.ticket_id) AS remaining_capacity
        FROM event_schedule es
        JOIN ticket t ON es.schedule_id = t.schedule_id
        LEFT JOIN ticket_sales ts ON t.ticket_id = ts.ticket_id
        JOIN venue v ON es.event_id = (SELECT event_id FROM event WHERE venue_id = v.venue_id)
        WHERE es.schedule_id = ?
        GROUP BY v.venue_id
    """,
        (schedule_id,),
    )

    remaining_capacity = cursor.fetchone()[0]
    print(f"Remaining capacity after cancellation: {remaining_capacity}")

    conn.commit()
    conn.close()


##################################^^^^^^User Ticket Management^^^^^^##############################################
import re


def is_valid_password(password):
    return len(password) >= 8


def is_valid_age(age):
    return age.isdigit() and 0 < int(age) < 120


def is_valid_phone(phone):
    phone_str = str(phone)
    return re.match(r"^\d{8}$", phone_str) is not None


def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


##################################^^^^^^data validate^^^^^^##############################################
def main():
    create_table()  # Ensure the table is created first
    conn = sqlite3.connect("project_database.db")
    cursor = conn.cursor()
    # Retrieve record from 'user' table
    cursor.execute("SELECT name FROM user WHERE name = 123")
    result = cursor.fetchone()
    if result is not None and result[0] == "123":
        print()
    else:
        conn = sqlite3.connect("project_database.db")
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO user (password, user_type, name, phone_number, email_address, gender, age)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            ("123", 0, "123", 12345678, "123456@gmail.com", "Male", 28),
        )
        conn.commit()
        conn.close()

    answer = int(
        input(
            "<Main Menu> \n1. Register Account \n2. Login Account\nEnter your choice: "
        )
    )
    while answer == 1:
        name = input("Enter name: ")
        # Check the name if it exits already
        conn = sqlite3.connect("project_database.db")
        cursor = conn.cursor()
        # Retrieve record from 'user' table
        cursor.execute("SELECT name FROM user WHERE name = ?", (name,))
        result = cursor.fetchone()
        if result is not None and result[0] == name:
            print("Username already exists")
            main()
        else:
            phone = input("Enter phone: ").strip()
            while not is_valid_phone(phone):
                print("Invalid phone number. Please enter a valid phone number.")
                phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            while not is_valid_email(email):
                print("Invalid email address. Please enter a valid email address.")
                email = input("Enter email: ").strip()

            gender = input("Enter gender: ").strip()
            while gender.lower() not in ["m", "f", "o"]:
                print("Invalid gender. Please enter 'M', 'F', or 'O'.")
                gender = input("Enter gender: ").strip()
            age = input("Enter age: ").strip()
            while not is_valid_age(age):
                print("Invalid age. Please enter a valid age between 1 and 119.")
                age = input("Enter age: ").strip()
            password = input("Enter password: ").strip()
            while not is_valid_password(password):
                print("Password must be at least 8 characters long.")
                password = input("Enter password: ").strip()
            user_type = 1
            add_user(password, user_type, name, phone, email, gender, age)
        main()
    while answer == 2:
        name = input("Input name: ")
        password = input("Input password: ")
        user_type = authenticate_user(name, password)  # Assign the returned user_type

        if user_type == 0:
            """
            # Check if the user is an Administrator
            user_type = int(input("Enter your user type (0 for Admin, 1 for User): "))
            """
            admin_menu(result, name)
        elif user_type == 1:  # Manage user
            user_menu(name, password)
    else:
        print("Invalid choice. Please try again.\n")
        main()


def admin_menu(result, name):
    while True:
        # admin_function
        admin_choose_function()
        table_choice = int(input("Choose a table: "))
        if table_choice == 1:  # User Management
            admin_user_management()
            function_choice = int(input("Choose your option: "))
            if function_choice == 1:  # View user
                view_user()
            elif function_choice == 2:  # Add user
                name = input("Enter name: ")
                if result is not None and result[0] == name:
                    print("Username already exists")
                else:
                    phone = input("Enter phone: ").strip()
                    while not is_valid_phone(phone):
                        print(
                            "Invalid phone number. Please enter a valid phone number."
                        )
                        phone = input("Enter phone: ").strip()
                    email = input("Enter email: ").strip()
                    while not is_valid_email(email):
                        print(
                            "Invalid email address. Please enter a valid email address."
                        )
                        email = input("Enter email: ").strip()
                    gender = input("Enter gender: ").strip()
                    while gender.lower() not in ["m", "f", "o"]:
                        print("Invalid gender. Please enter 'M', 'F', or 'O'.")
                        gender = input("Enter gender: ").strip()
                    age = input("Enter age: ").strip()
                    while not is_valid_age(age):
                        print(
                            "Invalid age. Please enter a valid age between 1 and 119."
                        )
                        age = input("Enter age: ").strip()
                    password = input("Enter password: ").strip()
                    while not is_valid_password(password):
                        print("Password must be at least 8 characters long.")
                        password = input("Enter password: ").strip()
                    user_type = int(input("Enter user type(admin:0/ user:1): "))
                    add_user(password, user_type, name, phone, email, gender, age)

            elif function_choice == 3:  # Edit user
                user_id = input("Enter user_id to be updated: ")
                # Check if user exists
                conn = sqlite3.connect("project_database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM user WHERE user_id = ?", (user_id,)
                )
                if cursor.fetchone()[0] == 0:
                    print("User not found")

                else:
                    new_name = input("Enter new name: ")
                    new_phone = input("Enter new phone number: ")
                    new_email = input("Enter new email: ")
                    new_gender = input("Enter new gender: ")
                    new_age = input("Enter new age: ")
                    new_password = input("Enter new password: ")
                    new_user_type = int(
                        input("Enter new user type (0 for Admin, 1 for User): ")
                    )
                    update_user(
                        user_id,
                        new_password,
                        new_user_type,
                        new_name,
                        new_phone,
                        new_email,
                        new_gender,
                        new_age,
                    )

                conn.close()
            elif function_choice == 4:  # Delete user
                del_user(int(input("Delete user_id: ")))

        elif table_choice == 2:  # Event Management
            print("\nThis is the Event Management section. Would you like to:")
            admin_event_management()
            function_choice = int(input("Choose your option: "))
            if function_choice == 1:  # View event
                view_event()
                view_event_schedule()
            elif function_choice == 2:  # Add event
                venue_id = input("Enter venue_id: ")
                event_name = input("Enter event name: ")
                event_description = input("Enter event description: ")
                add_event(venue_id, event_name, event_description)

                event_id = input("Enter event_id: ")
                schedule_name = input("Enter schedule name: ")
                schedule_start_time = input(
                    "Enter schedule start time (YYYY-MM-DD HH:MM:SS): "
                )
                schedule_end_time = input(
                    "Enter schedule end time (YYYY-MM-DD HH:MM:SS): "
                )
                schedule_description = input("Enter schedule description: ")
                add_event_schedule(
                    event_id,
                    schedule_name,
                    schedule_start_time,
                    schedule_end_time,
                    schedule_description,
                )
            elif function_choice == 3:  # Edit event
                event_id = input("Enter event_id to be updated: ")
                # Check if event exists
                conn = sqlite3.connect("project_database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM event WHERE event_id = ?", (event_id,)
                )
                if cursor.fetchone()[0] == 0:
                    print("Event not found")
                else:
                    new_venue_id = input("Enter new venue_id: ")
                    new_event_name = input("Enter new event name: ")
                    new_event_description = input("Enter new event description: ")
                    update_event(
                        event_id, new_venue_id, new_event_name, new_event_description
                    )
                conn.close()
            elif function_choice == 4:  # Edit event schedule:
                event_id = input("Enter event_id to be updated: ")
                # Check if event exists
                conn = sqlite3.connect("project_database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM event WHERE event_id = ?", (event_id,)
                )
                if cursor.fetchone()[0] == 0:
                    print("Event not found")
                else:
                    schedule_id = input("Enter schedule_id to be updated: ")
                    # Check if event exists
                    conn = sqlite3.connect("project_database.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT COUNT(*) FROM event_schedule WHERE schedule_id = ?",
                        (schedule_id,),
                    )
                    if cursor.fetchone()[0] == 0:
                        print("Schedule not found")
                    else:
                        new_schedule_name = input("Enter new schedule_name: ")
                        new_start_time = input(
                            "Enter new start_time(YYYY-MM-DD HH:MM:SS): "
                        )
                        new_end_time = input(
                            "Enter new end_time(YYYY-MM-DD HH:MM:SS): "
                        )
                        new_description = input("Enter new new_description: ")
                        update_event_schedule(
                            schedule_id,
                            event_id,
                            new_schedule_name,
                            new_start_time,
                            new_end_time,
                            new_description,
                        )
                    conn.close()
            elif function_choice == 5:  # Delete event
                del_event(int(input("Delete event_id: ")))

        elif table_choice == 3:  # Venue Management
            conn = sqlite3.connect("project_database.db")
            cursor = conn.cursor()
            # Retrieve record from 'user' table
            cursor.execute("SELECT * FROM user WHERE name = ?", (name,))
            user_record = cursor.fetchone()
            login_user_id = user_record[0]
            print("\nThis is the Venue Management section. Would you like to:")
            admin_venue_management()
            function_choice = int(input("Choose your option: "))
            if function_choice == 1:  # View venue
                view_venue()
            elif function_choice == 2:  # Add venue
                location = input("Enter location: ")
                capacity = input("Enter capacity: ")
                add_venue(location, capacity)
            elif function_choice == 3:  # Edit venue
                venue_id = input("Enter venue_id to be updated: ")
                # Check if venue exists
                conn = sqlite3.connect("project_database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM venue WHERE venue_id = ?", (venue_id,)
                )
                if cursor.fetchone()[0] == 0:
                    print("Venue not found")
                else:
                    new_location = input("Enter new location: ")
                    new_capacity = input("Enter new capacity: ")
                    update_venue(venue_id, new_location, new_capacity)
                conn.close()
            # elif function_choice == 4:  # Delete venue
            # del_venue(int(input('Delete venue_id: ')))

        elif table_choice == 4:  # Ticket Management
            print("\nThis is the Ticket Management section. Would you like to:")
            admin_ticket_management()
            function_choice = int(input("Choose your option: "))
            if function_choice == 1:  # View ticket
                view_tickets()
            elif function_choice == 2:  # Add ticket
                schedule_id = input("Enter schedule_id: ")
                price = input("Enter price: ")
                add_ticket(schedule_id, price)
            elif function_choice == 3:  # Edit ticket
                ticket_id = input("Enter ticket_id to be updated: ")
                # Check if ticket exists
                conn = sqlite3.connect("project_database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM ticket WHERE ticket_id = ?", (ticket_id,)
                )
                if cursor.fetchone()[0] == 0:
                    print("Ticket not found")
                else:
                    new_schedule_id = input("Enter new schedule_id: ")
                    new_price = input("Enter new price: ")
                    update_ticket(ticket_id, new_schedule_id, new_price)
                conn.close()
            elif function_choice == 4:  # Delete ticket
                del_ticket(int(input("Delete ticket_id: ")))

        elif table_choice == 5:  # Feedback Management
            print("\nThis is the Feedback Management section. Would you like to:")
            admin_feedback_management()
            function_choice = int(input("Choose your option: "))
            if function_choice == 1:  # View feedback
                view_feedback()
            elif function_choice == 2:  # Add feedback
                ticket_id = input("Enter ticket_id: ")
                comment = input("Enter comment: ")
                ratings = input("Enter ratings: ")
                add_feedback(ticket_id, comment, ratings)
            elif function_choice == 3:  # Edit feedback
                feedback_id = input("Enter feedback_id to be updated: ")
                # Check if feedback exists
                conn = sqlite3.connect("project_database.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT COUNT(*) FROM feedback WHERE feedback_id = ?",
                    (feedback_id,),
                )
                if cursor.fetchone()[0] == 0:
                    print("Feedback not found")
                else:
                    new_ticket_id = input("Enter new ticket_id: ")
                    new_comment = input("Enter new comment: ")
                    new_ratings = input("Enter new ratings: ")
                    update_feedback(
                        feedback_id, new_ticket_id, new_comment, new_ratings
                    )
                conn.close()
            elif function_choice == 4:  # Delete feedback
                del_feedback(int(input("Delete feedback_id: ")))
        elif table_choice == 6:
            admin_reporting_and_analytics()
        elif table_choice == 7:  # Exit the system
            print("Exiting the system. Goodbye!")
            main()
        else:
            print("Invalid choice. Please try again.")


def user_menu(name, password):
    while True:
        conn = sqlite3.connect("project_database.db")
        cursor = conn.cursor()
        # Retrieve record from 'user' table
        cursor.execute("SELECT * FROM user WHERE name = ?", (name,))
        user_record = cursor.fetchone()
        login_user_id = user_record[0]

        user_choose_function()
        table_choice = int(input("Choose a table: "))
        if table_choice == 1:  # Manage account
            print("1. View Personal Account \n2. Edit Personal Account")
            option = int(input("Option: "))
            if option == 1:
                view_PA(name, password)
            elif option == 2:
                new_user_name = input("Enter new_user_name: ")
                new_user_password = input("Enter new_user_password: ")
                new_user_pn = input("Enter new phone number: ")
                new_user_email = input("Enter new email: ")
                new_user_gender = input("Enter new gender: ")
                new_user_age = input("Enter new age: ")
                edit_PA(
                    name,
                    password,
                    new_user_name,
                    new_user_password,
                    new_user_pn,
                    new_user_email,
                    new_user_gender,
                    new_user_age,
                )
            else:
                print("invalid input")

        elif table_choice == 2:  # Manage event
            print("1. View Event List")
            option = int(input("Option: "))
            if option == 1:
                user_view_event()
            else:
                print("invalid input")

        elif table_choice == 3:  # Manage ticket
            print("1. Check and Purchase ticket")
            print("2. Reserve tickets")
            print("3. Cancel the ticket")
            option = int(input("Option: "))
            if option == 1:
                # check availability and purchase ticket
                check_tickets(login_user_id)
            elif option == 2:
                # view purchase ticket
                view_purchased_tickets(login_user_id)
            elif option == 3:
                # cancel the ticket
                cancel_tickets(login_user_id)
            else:
                print("invalid input")
        elif table_choice == 4:  # Manage feedback
            print("1. Submit Feedback \n2. View Feedback")
            option = int(input("Option: "))

            if option == 1:
                # Fetch the user's ticket sales records
                conn = sqlite3.connect("project_database.db")
                cursor = conn.cursor()
                cursor.execute(
                    """
                            SELECT ts.sales_id, e.event_name 
                            FROM ticket_sales ts 
                            JOIN ticket t ON ts.ticket_id = t.ticket_id 
                            JOIN event_schedule es ON t.schedule_id = es.schedule_id 
                            JOIN event e ON es.event_id = e.event_id 
                            WHERE ts.user_id = ?
                        """,
                    (login_user_id,),
                )
                sales_records = cursor.fetchall()

                if not sales_records:
                    print("No ticket sales found for your account.")
                else:
                    print("Available Ticket Sales:")
                    for idx, record in enumerate(sales_records):
                        sales_id, event_name = record
                        print(
                            f"{idx + 1}. Sales ID: {sales_id}, Event Name: {event_name}"
                        )
                    # Allow user to choose a sales record
                    record_choice = int(input("Choose a record by number: ")) - 1

                    if record_choice < 0 or record_choice >= len(sales_records):
                        print("Invalid choice. Please select a valid record number.")
                    else:
                        selected_sales_id = sales_records[record_choice][0]
                        comment = input("Enter comment: ")
                        ratings = input("Enter ratings: ")
                        add_feedback(selected_sales_id, comment, ratings)
                        print("Feedback submitted successfully.")

                conn.close()
            elif option == 2:
                user_view_feedback()
            else:
                print("invalid input")

        elif table_choice == 5:  # Exit the system
            print("Exiting the system. Goodbye!")
            main()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
