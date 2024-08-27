# Event Management System

### About

The Event Management System is a comprehensive application designed to facilitate the management of events, users, tickets, and feedback. The system utilizes a SQLite database to store and manage data efficiently. It allows administrators to manage user accounts, events, venues, ticket sales, and feedback, while also providing users with the ability to view events, purchase tickets, and submit feedback.

### Features

- User Management:
  User Types: Differentiate between admin (user_type: 0) and regular users (user_type: 1).
  Create, read, update, and delete user accounts based on user type.
- Event Management:
  Add, view, update, and delete events and their schedules.
- Venue Management:
  Manage venue details, including location and capacity.
- Ticket Management:
  Handle ticket creation, sales, and cancellations.
- Feedback System:
  Collect and manage user feedback on events.
- Reporting and Analytics:
  Generate reports and analyze ticket sales and user activities.

### Solution Architecture

The system architecture consists of the following components:
Database: SQLite database (project_database.db) to store all relevant data.
Backend Logic: Python scripts to handle business logic, database interactions, and user authentication.
User Interface: Command-line interface for user interactions.

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Ensure you have Python installed on your machine.
   Install required packages (if any):

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python event_management_system.py
```

### Usage

Upon running the application, users can choose from the following options:
User Management: Admins can manage user accounts.
Event Management: Admins can manage events and their schedules.
Venue Management: Admins can manage venue details.
Ticket Management: Admins can manage ticket sales and cancellations.
Feedback Management: Admins can collect and manage feedback.
Reporting and Analytics: Admins can generate reports and analyze data.
Users can also register, log in, view available events, purchase tickets, and provide feedback on events they attended.

### Tech Stack

Programming Language: Python
<br/> Database: SQLite
<br/> Libraries: sqlite3, datetime, csv
