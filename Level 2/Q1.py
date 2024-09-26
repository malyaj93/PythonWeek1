# Write a program to find the intersection (common elements) between two list

def common_elements(list1, list2):
    return [element for element in list1 if element in list2]

list1=list(map(int,input("Enter the elements of list1 : ").split()))
list2=list(map(int,input("Enter the elements of list2 : ").split()))

print("Common elements between list1 and list2 are : ", common_elements(list1,list2))