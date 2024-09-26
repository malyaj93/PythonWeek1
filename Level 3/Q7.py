# Input for the number of students & subjects
n = int(input("Enter the length which will be used for both lists: "))

list1 = []
list2 = []

for i in range(n):
    list1_values = input(f"Enter the values for list 1 {i + 1}: ")
    list2_values = input(f"Enter the values for list 2 corresponding to {list1_values}: ")

    # Append the inputs to the lists
    list1.append(list1_values)
    list2.append(list2_values)

# Using dictionary comprehension to construct the dictionary
created_dictionary = {list1[i]: list2[i] for i in range(len(list1))}

# Output the resulting dictionary
print("The newly created dictionary is :", created_dictionary)
