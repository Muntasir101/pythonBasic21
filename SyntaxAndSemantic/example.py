# Login test
username = input("Enter username: ")
password = input("Enter password: ")

username_admin = 'admin'
password_admin = '123456'

common_user_username = 'user'
common_user_password = 'password'

if username == username_admin or username == common_user_username:
    if password == password_admin:
        print("Admin Login Success.")
    elif password == common_user_password:
        print('Common user login successful')
    else:
        print("Invalid Password.")
else:
    print('Invalid Credentials.')




