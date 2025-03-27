import random

jokes = [
    "- Why did the scarecrow win an award? Because he was outstanding in his field!",
    "- What do you call a fake noodle? An impasta!", 
    "- Why couldn't the bicycle find its way home? It lost its bearings!",
]

PROMPT = "> What do you want? "
SORRY = "* Sorry, I only tell jokes."

def get_joke():
    return random.choice(jokes)

def interact():
    while True:
        try:
            user_input = input(PROMPT).strip().lower()

            if user_input in ['quit', 'exit', 'bye']:
                print("Goodbye!")
                break

            if "joke" in user_input:
                print(get_joke())
            else:
                print(SORRY)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    interact()