# 📊 Student Analytics Toolkit

A command-line Python application that analyzes student academic records and attendance using data stored in a JSON file. It provides insights such as student averages, toppers, and attendance reports through a simple menu-driven interface.

## Features

* View all student records
* Calculate average marks for each student
* Find the overall class topper
* Find subject-wise toppers
* Generate attendance reports
* Menu-driven CLI interface
* JSON-based data storage

## Technologies Used

* Python 3
* JSON (for data storage)
* File Handling

## Python Concepts Practiced

* Functions
* Modular Programming
* Packages and Modules
* Dictionaries
* Nested Dictionaries
* Loops and Nested Loops
* Dictionary Methods (`items()`, `values()`, `get()`)
* Dictionary Comprehensions
* JSON Handling (`json.load()`)
* File Handling
* Helper Functions
* Import Statements
* Conditional Statements (`if-elif-else`)
* String Formatting (f-strings)

## Project Structure

```text
student_analytics_toolkit/
│
├── analytics/
│   ├── __init__.py
│   ├── average_calc.py
│   ├── topper_finder.py
│   └── attendance_report.py
│
├── data.json
├── main.py
└── README.md
```

## Sample Student Structure

```json
{
    "Rahul": {
        "marks": {
            "Math": 92,
            "Science": 88,
            "English": 85
        },
        "attendance": {
            "present": 46,
            "total": 50
        }
    }
}
```

## Learning Outcomes

This project strengthened my understanding of modular programming by separating functionality into reusable modules. It also improved my knowledge of working with nested dictionaries, JSON-based data handling, packages, helper functions, dictionary comprehensions, and building a complete menu-driven command-line application while keeping the code organized and maintainable.