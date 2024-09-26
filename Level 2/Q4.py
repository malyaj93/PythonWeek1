# Write a program to enter a list and enter a number of how many times you want to right shift the list
# Then output the new list after shifts

def rotate_right(arr, D):
    D = D % len(arr)
    rotated_arr = arr[-D:] + arr[:-D]
    return rotated_arr

arr=list(map(int,input("Enter the elements : ").split()))
D = int(input("Enter the number of right shifts: "))
print("arr after rotation", rotate_right(arr, D))