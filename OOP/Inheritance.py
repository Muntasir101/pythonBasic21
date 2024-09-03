class University:
    # Constructor
    def __init__(self, university_name, university_code, university_location):
        self.university_name = university_name
        self.university_code = university_code
        self.university_location = university_location

    def greetings(self):
        print('Welcome to the University')


# Inheritance
class Department(University):
    def __init__(self, university_name, university_code, university_location, department_name, department_code):
        # call the constructor of parent class
        super().__init__(university_name, university_code, university_location)
        self.department_name = department_name
        self.university_code = department_code

        def department_info(self):
            print(f"Department Name: {self.department_name}")
            print(f"Department Code: {self.department_code}")


# create object
CSE_department = Department("MIT", 10101, 'USA', "Computer Science", "CSE111")

print(CSE_department.university_name)
print(CSE_department.department_name)