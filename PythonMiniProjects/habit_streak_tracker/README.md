# 🔥 Habit Streak Tracker

A command-line Habit Tracking application built using Python. The program allows users to create habits, track daily progress, maintain streaks, generate simple reports, and calculate a discipline score using JSON-based data storage.

## Features

* Add new habits
* Mark habits as completed
* Track habit streaks
* View all habits and current streaks
* Delete habits
* Generate a weekly summary report
* Calculate an overall discipline score
* Store data persistently using a JSON file

## Technologies Used

* Python 3
* JSON (for data storage)
* `os` module
* Functions and Modular Programming

## Python Concepts Practiced

* Reading and Writing JSON Files (`json.load()`, `json.dump()`)
* Data Persistence Without a Database
* Dictionaries and Nested Dictionaries
* Functions and Code Organization
* Loops and Conditional Statements
* File Path Handling with `os.path`
* User Input Validation
* Basic Data Analysis and Reporting
* Menu-Driven Program Flow

## Project Structure

```text
habit_streak_tracker/
│
├── app.py     # Menu and core program logic
├── data.json   # Persistent habit and streak storage
└── README.md
```

## Sample Data Format

```json
{
    "Reading": {
        "streak": 5
    },
    "Exercise": {
        "streak": 8
    }
}
```

## How to Run

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

4. Select an option from the menu:

```text
1. Add Habit
2. Mark Habit Completed
3. View Habits
4. Delete Habit
5. Weekly Report
6. Discipline Score
7. Exit
```

## Learning Outcomes

This project was built to practice Python fundamentals through a real-world habit tracking system. It strengthened my understanding of reading and writing structured data with `json.load()` and `json.dump()`, managing persistent application data without a database, working with nested dictionaries to store habit information and streak counts, and building a complete menu-driven CLI application with input validation and basic reporting.