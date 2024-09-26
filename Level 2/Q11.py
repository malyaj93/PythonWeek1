# Write a program to create a list of lists.
# The inner lists will consist of each individual characters of the string which were entered in the outer list Earlier

def split_strings(string_list):
    result = list(map(list, string_list))
    return result

string_list = input("Enter a list of strings: ").split()
print(split_strings(string_list))