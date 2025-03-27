import random

def main():
    print("I’m thinking of a number between 1 and 10. Try to guess it! 😏")
    
    random_number = random.randint(1, 10)
    lives = 6

    while True:
        hearts = f"Lives: {lives}"
        print(hearts)
        guess = int(input("Enter your guess: "))
        if lives == 0:
            print(f"Gameover, the number is {random_number}.")
        if guess > random_number:
            print("Go lower!")
            lives -= 1
        elif guess < random_number:
            print("Go high!")
            lives -= 1
        else:
            print("Yes! 🎉 You got it! Nice guessing! 😄")
            break

if __name__ == '__main__':
    main()
