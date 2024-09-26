# Write a program to find number of pairs from a list of numbers which are equal to the entered number "k"

def find_pairs(arr, k):
    pair = 0
    visited = set()

    for num in arr:
        complement = k - num
        if complement in visited:
            pair += 1
        visited.add(num)

    return pair


list1 = list(map(int, input("Enter the elements : ").split()))
k = int(input("Enter the number : "))
print(f"Pair count : ", find_pairs(list1, k))