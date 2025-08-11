# List to store student marks
students = []

# Subjects list
subjects = ["Maths", "English", "Hindi", "Science", "Computer Science"]

# Get number of students
num_students = int(input("Enter the number of students: "))

# Collect marks for each student
for i in range(num_students):
    student = {}
    name = input(f"\nEnter name of student {i+1}: ")
    student["Name"] = name
    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        student[subject] = mark
    students.append(student)

# Print all students' marks in a table
print("\nMarks of all students:")
header = ["Name"] + subjects
# Print header row
print("{:<20}".format(header[0]), end="")
for subj in header[1:]:
    print("{:<18}".format(subj), end="")
print()
print("-" * (20 + 18 * len(subjects)))
# Print each student's marks
for student in students:
    print("{:<20}".format(student["Name"]), end="")
    for subject in subjects:
        print("{:<18}".format(student[subject]), end="")
    print()

# Find and print the student with highest marks in each subject
#print("Topper in each subject:")
#for subject in subjects:
    #highest = max(students, key=lambda s: s[subject])
    # print(f"{subject}: {highest['Name']} ({highest[subject]})")


#print("\nList of students with highest marks in each subject (including ties):")
#for subject in subjects:
    #max_mark = max(student[subject] for student in students)
    #toppers = [student["Name"] for student in students if student[subject] == max_mark]
    #print(f"{subject}: {', '.join(toppers)} ({max_mark})")