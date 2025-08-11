# Declare an empty list
numbers = []

# Ask user for the number of elements
n = int(input("Enter the number of values you want to add to the list: "))

# Get input values from the user and add them to the list
for i in range(n):
    value = float(input(f"Enter value #{i+1}: "))
    numbers.append(value)

# Calculate and print the sum of the values
total = sum(numbers)
print("The sum of the values is:", total)