#Student Performance Analyzer

students = {
    "Rahul": [80, 75, 90],
    "Priya": [95, 92, 96],
    "Arjun": [60, 70, 65],
    "Sneha": [88, 85, 90]
}

for student, score in students.items():
    avg = sum(score) / len(score)
    print(f"{student} has an average score of {avg:.2f}")

topper = max(avg for avg in (sum(score) / len(score) for score in students.values()))
print(f"\nThe top performer is {topper:.2f}")

least_mrks = min(avg for avg in (sum(score) / len(score) for score in students.values()))
print(f"\nThe student with the least marks has an average score of {least_mrks:.2f}")

