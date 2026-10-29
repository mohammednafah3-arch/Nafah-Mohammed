student_name = input("Enter student name:")
department_name = input("Enter department name:")
length = len(student_name)
concatenate = student_name+department_name
print("\n--- Results ---")
print("Uppercase Name:",student_name.upper())
print("Lowercase Name:",student_name.lower())
print("Length of Student Name:",length)
print("Concatenation of student name and department name:",concatenate)
if "engineering" in department_name:
    print("Department contains the word engineering")
else:
    print("Department contain the word engineering")