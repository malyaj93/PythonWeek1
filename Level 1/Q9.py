# Function to count the frequency of elements in the list
def count_frequency(input_list):
    frequency = {}

    # Iterate through the list and count the frequency of each element
    for item in input_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    return frequency


# Taking input from the user as a space-separated list
user_input = input("Enter the list of numbers separated by spaces: ")

# Convert the input string to a list of integers
input_list = list(map(int, user_input.split()))

# Call the function and print the result
frequency_count = count_frequency(input_list)
print("Frequency count:", frequency_count)