from C_planets_trine import planet_combinations

def get_dasha_for_combinations(combinations):
    dasha_dict = {}
    for combo in combinations:
        dasha = input(f"Please provide the dasha for planet combination '{combo}': ")
        dasha_dict[combo] = dasha
    return dasha_dict

if __name__ == "__main__":
    dasha_info = get_dasha_for_combinations(planet_combinations)
    print("\nDasha information for each planet combination:")
    for combo, dasha in dasha_info.items():
        print(f"{combo}: {dasha}")