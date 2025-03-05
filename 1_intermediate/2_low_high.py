import random

NUM_ROUNDS = 5

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        user_input = input("Do you think your number is higher or lower than the computer's?: ").lower().strip()
        if user_input in ['higher', 'lower']:
            return user_input
        print("Please enter either 'higher' or 'lower'.")

def play_high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        
        your_number = generate_random_number()
        computer_number = generate_random_number()
        
        print(f"Your number is {your_number}")
        
        user_guess = get_user_guess()
        
        if user_guess == 'higher' and your_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif user_guess == 'lower' and your_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
    
    print("\nThanks for playing!")
    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

def main():
    play_high_low_game()

if __name__ == "__main__":
    main()