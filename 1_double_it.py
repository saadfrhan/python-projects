def double_until_threshold(start: int, threshold = 100):
    current = start
    results = []

    while current < threshold:
        current *= 2
        results.append(current)

    return results

def main():
    try:
        user_input = int(input("Enter a starting number: "))
        doubled_values = double_until_threshold(user_input)

        print("Doubled values:")
        for value in doubled_values:
            print(value)

    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    main()