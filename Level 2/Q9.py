# Write a program to catch index out of range exception

def get_element_from_list(my_list, index):
    try:
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"Index {index} is out of range for the list.")

my_list=list(map(int,input("Enter the elements : ").split()))
index = int(input("Enter the index to access: "))
get_element_from_list(my_list, index)