def calculate_planetary_weight(earth_weight):
    planetary_gravities = {
        'Mercury': 0.38,
        'Venus': 0.91,
        'Earth': 1.00,
        'Mars': 0.38,
        'Jupiter': 2.34,
        'Saturn': 1.06,
        'Uranus': 0.92,
        'Neptune': 1.19,
        'Pluto': 0.06
    }
    
    planetary_weights = {}
    for planet, gravity_factor in planetary_gravities.items():
        planetary_weights[planet] = round(earth_weight * gravity_factor, 2)

    return planetary_weights

def main():
    while True:
        try:
            earth_weight = float(input("Enter your weight on Earth (in pounds): "))

            planetary_weights = calculate_planetary_weight(earth_weight)

            print("\nYour weight on different planets:")
            for planet, weight in planetary_weights.items():
                print(f"{planet}: {weight} pounds")

            another_calculation = input("\nDo you want to calculate another weight? (y/n): ").lower()

            if another_calculation != 'y':
                break

        except ValueError:
            print("Please enter a valid number for weight.")
        
        except Exception as e:
            print(f"An error occured: {e}")
    
    print("\nThank you for using the Planetary Weight Calculator!")

if __name__ == "__main__":
    main()
    