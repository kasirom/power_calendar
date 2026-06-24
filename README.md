# power_calendar V.2
In the future, I will make the V.2 calendar more complete than V.1. 
I will introduce the program structure to you all, as below:


## Features

- **Event Management**: Add, edit, and delete events with ease.
- **Reminders**: Set reminders for important events with pre-notification options.
- **Contact Storage**: Store and manage important contact information.
- **Date Conversions**: Provides various date conversions (e.g., Hijri, Javanese).
- **Search Functionality**: Search for events by date or keyword.
- **Notifications**: Daily notifications for upcoming events.

## Project Structure

```
power-calendar
├── src
│   ├── main.py                # Main entry point of the application
│   ├── database.py            # Database connection and query management
│   ├── events_db.py           # CRUD operations for events
│   ├── contacts_db.py         # Storage and retrieval of contacts
│   ├── reminders_db.py        # Storage and retrieval of reminders
│   └── calendar_engine.py      # Date conversions and calculations
├── resources                   # Directory for additional resources (icons, images, etc.)
├── build                       # Directory for build scripts and specifications
│   ├── build_exe.cmd          # Command script for building the executable on Windows
│   ├── build_exe.sh           # Shell script for building the executable on Unix-like systems
│   └── power_calendar.spec     # PyInstaller specification file for building the executable
├── requirements.txt            # Python dependencies for the project
├── pyproject.toml             # Project configuration and dependencies
└── README.md                   # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/kasirom/power_calendar.git
   cd power-calendar
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Building Executable

To build the executable package, use the provided scripts in the `build` directory:

- For Windows:
  ```
  build/build_exe.cmd
  ```

- For Unix-like systems:
  ```
  sh build/build_exe.sh
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
====================================================================================================
Currently I am sharing version 1 first
I'm currently sharing Version 1:
# PowerCalendar ULTIMATE
Multi-calendar project skeleton.
ULTIMATE POWER CALENDAR

Hello, it's BAZORA again. I'm Mbah Suro, aka Kasirom JhonyROW.
To create a powerful "Power Calendar Ultimate" application with a modern GUI,
a full-fledged database, and more comprehensive forecast details, here are some development suggestions:

1. Modern GUI with Qt Designer or QML
We'll use Qt Designer to visually design the GUI.
Or use QML to create a more modern and responsive interface.
Add a modern theme using a library like Qt Style Sheets (QSS).

2. Full Database Integration
Use a database like SQLite to store event, user, and forecast results.
Example tables:

users: Stores user data (name, address, date of birth).

events: Stores event data (date, description).

predictions: Stores forecast results for future reference.
SQLite integration example:
========================

# filepath: c:Kalender\database.py
import sqlite3

class Database:
    def __init__(self, db_name="calendar.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                address TEXT,
                birth_date TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                description TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                prediction TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        self.conn.commit()
================================
3. More Detailed Predictions
Forecast logic based on Javanese-Indonesian primbon, feng shui, or zodiac signs.
Use an astrology library to calculate planetary positions and provide more accurate predictions.
Additional examples of forecast logic:
=================================
# filepath: c:\calendar_engine.py
def analis_primbon(self, nama, alamat, dt):
weton = get_weton(dt)
zodiak = self.get_zodiac(dt)

hasil = []
hasil.append("=== HASIL ANALYSIS PRIMBON ===")
hasil.append(f"Name : {nama}")
hasil.append(f"Address : {address}")
hasil.append(f"Birth : {dt:%d-%m-%Y}")
hasil.append("")
hasil.append(weton)
hasil.append(f"Zodiac : {zodiak}")
hasil.append("")

# Additional Logic
hasil.append("Fortune : Smooth if consistent")
hasil.append("Soulmate : Compatible with patient character")
hasil.append("Career : Good in technology / business") 

return "\n".join(result)

def get_zodiac(self, dt): 
zodiacs = [ 
("Capricorn", (1, 20)), ("Aquarius", (2, 19)), 
("Pisces", (3, 20)), ("Aries", (4, 20)), 
("Taurus", (5, 21)), ("Gemini", (6, 21)), 
("Cancer", (7, 22)), ("Leo", (8, 22)), 
("Virgo", (9, 23)), ("Libra", (10, 23)), 
("Scorpio", (11, 22)), ("Sagittarius", (12, 21)), 
("Capricorn", (12, 31)) 
] 
for zodiac, (month, day) in zodiac: 
if (dt.month, dt.day) <= (month, day): 
returns zodiac 
return "Capricorn"
=============================
4. Data Export
Add a feature to export forecast and event data to PDF or Excel.
Use libraries like openpyxl for Excel and reportlab for PDF.
5. Notifications and Reminders
Add event reminders using desktop or email notifications.
Use libraries like plyer for notifications.
6. Internationalization
Add support for multiple languages ​​using the Qt Linguist library.
With these improvements, your application will be more modern, feature-rich, and engaging for users.

Install:
pip install PySide6 hijri-converter

Run:
python main.py

