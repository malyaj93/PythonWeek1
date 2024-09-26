# writing a program to calculate sum of digits at the odd places using for loop

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
Sum = 0
for i in range(start,end+1,2):
    Sum+=i
print("Sum of odd numbers: ",Sum)