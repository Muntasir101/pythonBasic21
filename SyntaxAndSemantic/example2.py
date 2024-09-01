"""
Discount for 1000 or more tk purchase: 10tk discount
for more than 5000 tk purchase: 60tk discount

input: purchase amount
output: discount amount and after discount, how much amount to pay

example:
purchase amount : 1200
Discount amount : 10
Final amount to pay: 1190
"""

purchase_amount = int(input("Please Enter your purchase amount: "))
discount = 0

if purchase_amount >= 5000:
    discount = 60
    print("Your Discount Amount: ", discount)
    Final_amount_to_pay = purchase_amount - discount
    print("After Discount you have to pay: ", Final_amount_to_pay)
elif purchase_amount >= 1000:
    discount = 10
    print("Your Discount Amount: ", discount)
    Final_amount_to_pay = purchase_amount - discount
    print("After Discount you have to pay: ", Final_amount_to_pay)
else:
    print('Sorry! No Discount.You have to pay: ', purchase_amount)
