# import math
# print(math.sqrt(16))


# from math import *
# print(sqrt(25))

from datetime import date, datetime, timedelta

print(date.today())
print(datetime.now().time())
print(datetime.now())
formatted_date = datetime.now().strftime("%d-%m-%Y %H:%M")
print(formatted_date)

current_date = date.today()
new_date = current_date + timedelta(days=10)
print(new_date)
