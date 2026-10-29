students=[]
n=int(input("Enter the number of students:"))
for i in range(n):
    print(f"\n Enter details of student{i+1}")
    name=input("Enter student name:")
    usn=input("Enter usn:")
    mark1=float(input("Enter marks in course1:"))
    mark2=float(input("Enter marks in course2:"))
    mark3=float(input("Enter marks in course3:"))
    total=mark1+mark2+mark3
    average=total/3
students.append([name,usn,mark1,mark2,mark3,total,average]) 
print("\n"+"="*94)
print("STUDENTS MARKS REPORT")
print("="*94)
print(f"{'Name':<15}{'usn':<15}{'course1':>10}"
f"{'course2':>10}{'course3':>10}" 
f"{'total':>10}{'average':>10}")
print("="*94)

for student in students:
    name,usn,course1,course2,course3,total,average=student
    print(f"{name:<15}{usn:<15}{course1:>10.2f}"
    f"{course2:>10.2f}{course3:>10.2f}"
    f"{total:>10.2f}{average:>10.2f}")
    
print("="*94)