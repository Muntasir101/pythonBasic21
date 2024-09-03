class University:
    university_name = "MIT"
    university_code = 1123
    university_location = "USA"

    def greetings(self):
        print('Welcome to the University')


class College:
    college_name = "DC"
    college_code = 101
    college_location = "Dhaka"


# create object
CSE_department = University()
print(CSE_department.university_name)
CSE_department.greetings()

# create object
IT_department = University()
print(IT_department.university_name)
IT_department.greetings()

# create object
CC_department = University()
print(CC_department.university_name)
CSE_department.greetings()

# create object
hsc_24 = College()
print(hsc_24.college_code)

# create object
hsc_25 = College()
print(hsc_25.college_code)

# create object
hsc_26 = College()
print(hsc_26.college_code)
