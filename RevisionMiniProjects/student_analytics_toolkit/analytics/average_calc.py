def calculate_average(marks):
    total = sum(marks.values())
    count = len(marks)
    return total/count

def subject_wise_class_average(students):
    subject_totals = {}  #total marks of each student for a subject
    subject_counts = {}  # number of students who gave the subject

    for student_data in students.values():
        for subject, score in student_data["marks"].items():
            subject_totals[subject] = subject_totals.get(subject, 0) + score
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return {
        subject: subject_totals[subject] / subject_counts[subject]
        for subject in subject_totals  #dictionary comprehension
    }