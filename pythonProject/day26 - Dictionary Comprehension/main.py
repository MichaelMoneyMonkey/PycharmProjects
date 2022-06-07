import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# new_dict = {new_key: new_value for (key,value) in dict.items() if test}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


weather_f = {key: value * 9 / 5 + 32 for (key, value) in weather_c.items()}

# Write your code 👇 below:

print(weather_f)


student_dict = {
    "student": ["Angela", "Michael", "Megan"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

    import pandas

    student_data_frame = pandas.DataFrame(student_dict)
    print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
    print(row.score)
