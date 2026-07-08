import json

from analytics.average_calc import calculate_average
from analytics.topper_finder import find_overall_topper, find_subject_toppers
from analytics.attendance_report import generate_attendance_report


def load_data(filename="data.json"):
    with open(filename, "r") as file:
        return json.load(file)


def view_all_students(students):
    for name, data in students.items():
        print(f"\n{name}")
        print(f"  Marks      : {data['marks']}")
        print(f"  Attendance : {data['attendance']['present']}/{data['attendance']['total']}")


def show_average_calculator(students):
    for name, data in students.items():
        average = calculate_average(data["marks"])
        print(f"{name}: {round(average, 2)}")


def show_overall_topper(students):
    name, average = find_overall_topper(students)
    print(f"Overall topper: {name} ({round(average, 2)} average)")


def show_subject_toppers(students):
    toppers = find_subject_toppers(students)
    for subject, (name, score) in toppers.items():
        print(f"{subject}: {name} ({score})")


def show_attendance_report(students):
    report = generate_attendance_report(students)
    for name, percentage in report.items():
        print(f"{name}: {percentage}%")


def show_menu():
    print("\n" + "=" * 35)
    print("STUDENT ANALYTICS TOOLKIT")
    print("=" * 35)
    print("1. View all students")
    print("2. Average calculator")
    print("3. Topper finder (overall)")
    print("4. Topper finder (per subject)")
    print("5. Attendance report")
    print("6. Exit")


def main():
    students = load_data()

    while True:
        show_menu()
        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            view_all_students(students)
        elif choice == "2":
            show_average_calculator(students)
        elif choice == "3":
            show_overall_topper(students)
        elif choice == "4":
            show_subject_toppers(students)
        elif choice == "5":
            show_attendance_report(students)
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
