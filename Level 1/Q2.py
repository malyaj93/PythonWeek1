# Defining the function to count letters and digits
def count_letters_and_digits(s):
    total_digits = 0
    total_letters = 0

    for i in s:
        if i.isnumeric():
            total_digits += 1
        else:
            total_letters += 1

    print(f"Alphabets: {total_letters} & Number: {total_digits}")


# Inputing the value and calling the above function
string1 = input("Enter a string:")
count_letters_and_digits(string1)