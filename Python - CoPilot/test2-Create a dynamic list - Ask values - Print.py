# Declare an empty list
my_list = []

# Ask user for the length of the list
length = int(input("Enter the length of the list: "))

# Ask user to provide values for the list
for i in range(length):
    value = input(f"Enter value {i+1}: ")
    my_list.append(value)

# Print the list
print("The list is:", my_list)