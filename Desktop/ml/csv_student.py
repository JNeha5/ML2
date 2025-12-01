import csv
from dataset_student import students_data

filename="student_records.csv"

fields= ['roll_no', 'name', 'subject', 'gpa', 'year']

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)

    for row in students_data:
        writer.writerow(row)

