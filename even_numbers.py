def is_even(number):
    return number % 2 == 0

number = int(input("Enter number: "))
if is_even(number):
    print(number, "is even")
else:
    print(number, "is odd")