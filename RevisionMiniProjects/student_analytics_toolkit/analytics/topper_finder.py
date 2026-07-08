from analytics.average_calc import calculate_average

def find_overall_topper(students):
    topper_name = None
    highest_average = -1

    for name, data in students.items():
        average = calculate_average(data["marks"])
        if average > highest_average:
            highest_average = average
            topper_name = name

    return topper_name, highest_average

def find_subject_toppers(students):
    subject_toppers = {}
 
    for name, data in students.items():
        for subject, score in data["marks"].items():
            current_best = subject_toppers.get(subject)
 
            if current_best is None or score > current_best[1]:
                subject_toppers[subject] = (name, score)
 
    return subject_toppers