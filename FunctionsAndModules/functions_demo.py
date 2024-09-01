def multiple_print():
    print("Hello world !!")


for i in range(10):
    multiple_print()


# function defining
def summation():
    print(10 + 20)


# function calling
summation()


def subtraction():
    print(10 - 5)
    summation()


subtraction()


# function with return values
def add(a, b):
    return a + b


result = add(30, 70)
print(result)

print(add(100, 300))
