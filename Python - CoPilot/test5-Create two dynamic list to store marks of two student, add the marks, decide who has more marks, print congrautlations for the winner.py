# Create two lists to store marks for Tejveer and Sukriti
subjects = ["English", "Maths", "Science", "Computer", "Hindi"]

tejveer = []
sukriti = []

print("Enter marks for Tejveer:")
for subject in subjects:
    mark = int(input(f"{subject}: "))
    tejveer.append(mark)

print("\nEnter marks for Sukriti:")
for subject in subjects:
    mark = int(input(f"{subject}: "))
    sukriti.append(mark)

# Calculate total marks
total_tejveer = sum(tejveer)
total_sukriti = sum(sukriti)

# Decide and print the winner
if total_tejveer > total_sukriti:
    print(f"\nCongratulations Tejveer! You scored {total_tejveer} marks.")
elif total_sukriti > total_tejveer:
    print(f"\nCongratulations Sukriti! You scored {total_sukriti} marks.")
else:
    print(f"\nIt's a tie! Both scored {total_tejveer} marks.")