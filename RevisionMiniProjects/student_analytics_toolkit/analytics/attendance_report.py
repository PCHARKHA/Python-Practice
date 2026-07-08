def calculate_attendance_percentage(attendance):
    present = attendance["present"]
    total = attendance["total"]
    return (present / total) * 100


def generate_attendance_report(students):
    report = {}

    for name, data in students.items():
        percentage = calculate_attendance_percentage(data["attendance"])
        report[name] = round(percentage, 2)

    return report