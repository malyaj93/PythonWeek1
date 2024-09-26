# Writing a program to find the sum of digits of entered number until only single digit is left

def sum_of_digits(num):
    total_sum = 0

    while num > 0:
        total_sum += num % 10
        num //= 10

    return total_sum


def single_digit_sum(num):
    while num >= 10:
        num = sum_of_digits(num)
    return num


num = int(input("Enter the number : "))
initial_sum = sum_of_digits(num)
print(f"Sum_of_digits = {initial_sum}")

final_sum = single_digit_sum(initial_sum)
print(f"Final Output = {final_sum}")