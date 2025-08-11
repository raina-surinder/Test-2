# Create two empty lists
list1 = []
list2 = []

# Ask user for the length of the lists
length = int(input("Enter the length of the lists: "))

# Get values for the first list
print("Enter values for the first list:")
for i in range(length):
    value = int(input(f"Value {i+1}: "))
    list1.append(value)

# Get values for the second list
print("Enter values for the second list:")
for i in range(length):
    value = int(input(f"Value {i+1}: "))
    list2.append(value)

# Add corresponding values from both lists
sum_list = []
for i in range(length):
    sum_list.append(list1[i] + list2[i])

# Print the resulting list
print("Sum of corresponding values:", sum_list)