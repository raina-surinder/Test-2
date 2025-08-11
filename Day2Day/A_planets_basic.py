# List of planets with their information

planets = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]

# Print the list in tabular format
print("{:<3} {:<60}".format("No", "Planet"))
print("-" * 65)
for idx, planet in enumerate(planets, start=1):
    print("{:<3} {:<60}".format(idx, planet))