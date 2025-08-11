num_elements = int(input("Enter the number of elements: "))
my_list = []
for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)
print("The list is:", my_list)