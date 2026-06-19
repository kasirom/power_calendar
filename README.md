# power_calendar


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
