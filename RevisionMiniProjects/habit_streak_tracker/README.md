# Habit Streak Tracker

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
* JSON File Handling
* OS Module
* Functions and Modular Programming

## Concepts Demonstrated

* Reading and writing JSON files
* Data persistence
* Dictionary operations
* Functions and code organization
* Loops and conditional statements
* File path handling with `os.path`
* User input validation
* Basic data analysis and reporting

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

## Key Learnings

* Using `json.load()` to read structured data from a JSON file.
* Using `json.dump()` to save Python dictionaries to a JSON file.
* Managing persistent application data without a database.
* Working with nested dictionaries for storing habit information and streak counts.
* Updating and tracking streak-based progress over time.

## Purpose

This project was built to practice Python fundamentals, particularly JSON handling, file operations, dictionaries, functions, and menu-driven application development through a real-world habit tracking system.
