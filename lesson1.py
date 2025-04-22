x1 = input("Enter the first number: ")
x2 = input("Enter the second number: ")
x3 = input("Enter the third number: ")
x4 = input("Enter the fourth number: ")
x5 = input("Enter the fifth number: ")
x6 = input("Enter the sixth number: ")
x7 = input("Enter the seventh number: ")
numbers = [x1, x2, x3, x4, x5, x6, x7]

# Calculate the average 
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += float(num)
    return total / len(numbers)

# Calculate the average
average = calculate_average(numbers)
print("The average is:", average)


