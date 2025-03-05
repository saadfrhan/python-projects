import random

def generate_random_numbers(count=10, min=1, max=100):
    return [random.randint(min, max) for _ in range(count)]

def main():
    random_nums = generate_random_numbers()

    for num in random_nums:
        print(num)

if __name__ == "__main__":
    main()