# defining a function to check for the input number
def check_for_number(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Consultadd - Python Training")
    elif number % 3 == 0:
        print("Consultadd")
    elif number % 5 == 0:
        print("Python Training")
    else:
        print("The number is not divisible by 3 or 5")

# calling the function and entering the number
number = int(input("Enter a number: "))
check_for_number(number)