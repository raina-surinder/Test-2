import itertools
from A_planets_basic import planets
from tabulate import tabulate

# Generate all combinations of 3 planets
planet_combinations = list(itertools.combinations(planets, 3))

# Prepare data for tabulation
table = [list(combo) for combo in planet_combinations]
headers = ["Planet 1", "Planet 2", "Planet 3"]

print(tabulate(table, headers=headers, tablefmt="grid"))
