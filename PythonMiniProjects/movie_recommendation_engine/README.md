# 🎬 Movie Recommendation Engine

A command-line Python application that recommends movies based on genres and allows users to manage their own movie collection stored in a JSON file.

## Features

* View available genres
* View movies by genre
* Search a movie by title
* Add a new movie
* Update movie details
* Delete a movie
* View top-rated movies
* Get a random movie recommendation

## Technologies Used

* Python 3
* JSON (for data storage)
* File Handling
* `random` module

## Python Concepts Practiced

* Functions
* Lists
* Dictionaries
* Nested Data Structures (Dictionary of Lists)
* Loops and Nested Loops
* `enumerate()`
* JSON Handling (`json.load()` and `json.dump()`)
* File Handling
* Helper Functions
* CRUD Operations (Create, Read, Update, Delete)
* Sorting using `sorted()` and `lambda`
* Random Selection using `random.choice()`
* String Methods (`strip()`, `title()`, `lower()`)

## Project Structure

```text
movie_recommendation_engine/
│
├── main.py
├── data.json
└── README.md
```

## Sample Movie Structure

```json
{
    "Sci-Fi": [
        {
            "title": "Interstellar",
            "rating": 9.2,
            "year": 2014,
            "mood": "motivational"
        }
    ]
}
```

## Learning Outcomes

This project strengthened my understanding of working with nested data structures, JSON-based data persistence, searching and sorting algorithms, helper functions for code reusability, and building a complete menu-driven CLI application in Python.
