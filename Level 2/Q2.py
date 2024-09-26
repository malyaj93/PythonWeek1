# Write a program to return a list of unique number from the input list of numbers

def unique_list(numbers):
    uni=list(set(numbers))
    return uni

list1=list(map(int,input("Enter the elements : ").split()))
print("Unique elements in the list are : ", unique_list(list1))