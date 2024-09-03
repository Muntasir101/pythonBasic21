class University:
    # constructor
    def __init__(self, university_name, university_code, university_location):
        self.university_name = university_name
        self.university_code = university_code
        self.university_location = university_location

    def greetings(self):
        print('Welcome to the University')


# create object
CSE_department = University("MIT", 10101, 'USA')
CSE_department2 = University("Oxford", 155, "UK")
CSE_department3 = University("Dhaka University", 111, 'Bangladesh')

