car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

user1_details = {
    "first_name": "Mr.",
    "last_name": "Smith",
    "email": "smith@gmail.com",
    "password": 123456,
    "skills": ["javascript", "python", "java"],
    "address": {
        "present_address": {
            "city": "dhaka",
            "road": 123
        },
        "permanent_address": {
            "city": "NY",
            "road": 12345
        }
    }
}
print(user1_details["address"]["permanent_address"]["city"])

user2_details = {
    "first_name": "Mr.",
    "last_name": "Wood",
    "email": "Wood@gmail.com",
    "password": "123456",
    "skills": ["javascript", "python", "java"]
}

user_details_list = [user1_details, user2_details]
print(user_details_list)
