import json
import os

def load_habits():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "habits.json")

    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r") as file:
        return json.load(file)


def save_habits(habits):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "habits.json")

    with open(file_path, "w") as file:
        json.dump(habits, file, indent=4)


def view_habits(habits):
    if not habits:
        print("No habits found.")
        return

    print("\n===== Your Habits =====")

    for habit_name, details in habits.items():
        print(f"{habit_name} : {details['streak']} days")


def add_habits(habits):
    habit_name = input("Enter habit name: ").strip().title()

    if habit_name in habits:
        print("This habit already exists")

    else:
        habits[habit_name] = {
            "streak": 0
        }

        save_habits(habits)

        print("Habit added successfully")
        view_habits(habits)


def mark_completed(habits):
    view_habits(habits)

    habit_name = input(
        "Enter habit to mark it completed: "
    ).strip().title()

    if habit_name not in habits:
        print("Habit not found")

    else:
        habits[habit_name]["streak"] += 1

        save_habits(habits)

        print(f"\n{habit_name} completed!")
        print(f"Current Streak : {habits[habit_name]['streak']} days")

def delete_habits(habits):
    view_habits(habits)

    habit_name = input("Enter habit to delete: ").strip().title()

    if habit_name not in habits:
        print("Habit not found")

    else:
        del habits[habit_name]

        save_habits(habits)

        print(f"{habit_name} deleted successfully")
        view_habits(habits)


def weekly_reports(habits):
    if not habits:
        print("No habits found.")
        return

    total_habits = len(habits)

    total_streak_days = 0

    for details in habits.values():
        total_streak_days += details["streak"]

    best_habit = max(
        habits,
        key=lambda habit: habits[habit]["streak"]
    )

    print("\n===== Weekly Report =====")
    print(f"Total Habits      : {total_habits}")
    print(f"Total Streak Days : {total_streak_days}")
    print(f"Best Habit        : "
        f"{best_habit} ({habits[best_habit]['streak']} days)"
    )


def discipline_score(habits):
    if not habits:
        print("No habits found.")
        return

    total_streak_days = 0

    for details in habits.values():
        total_streak_days += details["streak"]

    maximum_possible = len(habits) * 7

    score = (
        total_streak_days / maximum_possible
    ) * 100

    print("\n===== Discipline Score =====")
    print(f"Discipline Score : {score:.2f}%")

    if score >= 80:
        print("Excellent consistency!")
    elif score >= 60:
        print("Good consistency.")
    else:
        print("Needs improvement.")


while True:
    print("\n===== Habit Streak Tracker =====")
    print("1. Add Habit")
    print("2. Mark Habit Completed")
    print("3. View Habits")
    print("4. Delete Habit")
    print("5. Weekly Report")
    print("6. Discipline Score")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        habits = load_habits()
        add_habits(habits)

    elif choice == "2":
        habits = load_habits()
        mark_completed(habits)

    elif choice == "3":
        habits = load_habits()
        view_habits(habits)

    elif choice == "4":
        habits = load_habits()
        delete_habits(habits)

    elif choice == "5":
        habits = load_habits()
        weekly_reports(habits)

    elif choice == "6":
        habits = load_habits()
        discipline_score(habits)

    elif choice == "7":
        print("Exiting Habit Tracker...")
        break

    else:
        print("Invalid choice. Please try again.")