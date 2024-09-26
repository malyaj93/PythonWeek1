# Writing a program to calculate  Least Common Multiple (LCM) of two numbers

def calculate_lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while True:
        if (z % x == 0) and (z % y == 0):
            lcm = z
            break
        z += 1

    return lcm


n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
print(f"LCM of {n1} and {n2} is: ", calculate_lcm(n1, n2))