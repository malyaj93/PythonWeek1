# Write a program to reverse entered number

def reverse_num(num):
    rev = 0

    while num > 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num //= 10
    return rev


num = int(input("Enter the number : "))
print("Reversed number : ", reverse_num(num))