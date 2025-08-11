from A_planets_basic import planets
from tabulate import tabulate

planets_attributes = []

for planet in planets:
    print(f"Enter 3 attributes for {planet}:")
    attributes = []
    for i in range(1, 4):
        attr = input(f"Attribute {i}: ")
        attributes.append(attr)
    planets_attributes.append({'name': planet, 'attributes': attributes})

table = []
for planet in planets_attributes:
    row = [planet['name']] + planet['attributes']
    table.append(row)

headers = ["Planet", "Attribute 1", "Attribute 2", "Attribute 3"]
print(tabulate(table, headers=headers, tablefmt="grid"))