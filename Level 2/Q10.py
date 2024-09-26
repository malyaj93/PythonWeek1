# We are making n stone piles! The first pile has n stones.
# If n is even, then all piles have an even number of stones.
# If n is odd, all piles have an odd number of stones.
# Each pile must have more stones than the previous pile but as few as possible.
# Write a Python program to find the number of stones in each pile.

def stone_piles(n):
    stones = []

    # Check if n is even or odd
    if n % 2 == 0:
        # If n is even, use even numbers
        for i in range(2, n+1, 2):
            stones.append(i)
    else:
        # If n is odd, use odd numbers
        for i in range(1, n+1, 2):
            stones.append(i)

    return stones

# Input n (number of stones in the first pile)
n = int(input("Enter the number of stones in the first pile (n): "))

# Get the list of stones in each pile
result = stone_piles(n)

# Output the result
print("Stones in each pile =", result)
