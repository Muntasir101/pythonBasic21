# This is single line comment

"""
username: admin
password: 123456
role: admin
email: admin@mail.com
"""

password = 123456

"""
Data Types:
1. int
2. float
3. str
4. bool
"""

marks = 85  # integer
tax_rate = 10.5  # float
username = "student_1"  # string
active_status = True  # boolean

a = 100
b = 20
c = a / b  # 5

d = 10
# d = d + 1  # 11
d += 1  # 11
e = c + d  # 5 + 11 = 16

"""
Operators:
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
"""

pass_marks = 40
my_mark = 40
minimum_attendance = 80
my_attendance = 70

if my_mark >= pass_marks and my_attendance >= minimum_attendance:
    print("Congratulations !!! You will Get a Certificate")
else:
    print("Sorry !!!")

"""
Control flow:
Conditional statement: if, elif, else
Loops: for, while
"""

weather = "rainy"

if weather == "sunny":
    print("Let's play some games")
else:
    print("Try another day")

print("Grade List")
print("==========")

marks = int(input("Please Enter your Marks: "))

if marks >= 90:
    grade = "A"
    print(grade)
elif marks >= 70:
    grade = "B"
    print(grade)
elif marks >= 50:
    grade = "C"
    print(grade)
elif marks >= 40:
    grade = "D"
    print(grade)
else:
    grade = "F"
    print(grade)

# Loops
# for _ in range(5):
for i in range(5):
    print("Hello world!!")
