# Write a program to check if the entered sentence or string starts with the entered string.
# The cases should match as well

starts_with = lambda input_string, given_char: input_string.startswith(given_char)

input_string = input("Enter a string: ")
given_char = input("Enter a character: ")

if starts_with(input_string, given_char):
    print(f"The sentence starts with the entered character")
else :
    print(f"The sentence does not starts with the entered character")