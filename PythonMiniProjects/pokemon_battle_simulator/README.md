# ⚔️ Pokemon Battle Simulator

A command-line Python application that simulates turn-based Pokemon battles, complete with type effectiveness, critical hits, accuracy checks, and PP management, built using object-oriented programming.

## Features

* Choose from 4 starter Pokemon (Fire, Water, Grass, Electric)
* Random opponent selection from the remaining starters
* Turn-based battle system with speed-based turn order
* Type effectiveness system (super effective / not very effective)
* Random damage variance (90–110%) on every hit
* Critical hit chance (10%)
* Move accuracy checks (moves can miss)
* PP (Power Points) tracking per move
* Full battle log summary printed at the end of the fight
* ASCII art banners for title, win, and loss screens

## Technologies Used

* Python 3
* `random` module
* Object-Oriented Programming (OOP)

## Python Concepts Practiced

* Classes and Objects
* Constructors (`__init__`)
* Instance Methods and Attributes
* Composition (a `Pokemon` holds a list of `Move` objects)
* `isinstance()` for type checking
* Lists and List Comprehensions
* Dictionaries (type effectiveness chart with tuple keys)
* Loops (`for`, `while`) and Nested Loops
* `enumerate()`
* Conditional Logic
* Exception Handling (`try` / `except ValueError`)
* Random Selection and Ranges (`random.choice()`, `random.randint()`, `random.uniform()`)
* String Formatting (f-strings)
* Modules and Imports Across Multiple Files
* Helper Functions

## Project Structure

```text
pokemon_battle_simulator/
│
├── classes.py     # Pokemon and Move classes
├── battle.py      # Battle logic (turns, damage, type chart, win/loss)
├── ascii_art.py   # Title banner, win/lose screens, type art
├── main.py        # Entry point — pick a starter and fight
└── README.md
```

## Sample Pokemon Definition

```python
ember = Move("Ember", "Fire", power=40, accuracy=100, pp=25)

charmander = Pokemon(
    name="Charmander",
    pokemon_type="Fire",
    level=12,
    max_hp=90,
    attack=45,
    defense=38,
    speed=65
)

charmander.add_move(ember)
```

## How to Run

Keep all four `.py` files in the same folder, then run:

```bash
python main.py
```

Pick a starter (1–4), an opponent is chosen at random from the rest, and the battle plays out turn by turn until one Pokemon faints.

## Learning Outcomes

This project strengthened my understanding of object-oriented design in Python, specifically how separate classes (`Pokemon`, `Move`, `Battle`) can be composed together to model real-world interactions. It also reinforced working with dictionaries as lookup tables (the type chart), handling randomness in a controlled way (damage variance, critical hits, accuracy), and structuring a multi-file Python project with clean imports instead of one large script.