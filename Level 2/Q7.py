# Write a program to find the median of an entered list of numbers

def find_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)
    print(f"Sorted List: ", sorted_list)

    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

    return median


number_list = list(map(int, input("Enter the elements : ").split()))
print(f"Median: ", find_median(number_list))