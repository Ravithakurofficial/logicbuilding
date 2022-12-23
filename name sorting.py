#Given the names and grades for each student in a class of  students,
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

a = int(input("enter number of inputs"))
student_name = []
for i in range(0,a):
    name = input("enter the name : ")
    marks = int(input("enter marks : "))
    student_name.append([name,marks])

print(student_name)
marks_wise = sorted(list(set([x[1] for x in student_name])))

print(marks_wise)

#makeing 2nd lowest score
seconde_lowest = marks_wise[1]

#checking if any of the student have same marks
lowest_marks = []
for name in student_name:
     if seconde_lowest == student_name[0]:
        lowest_marks.append(name)

for student in sorted(lowest_marks):
    print(name)


