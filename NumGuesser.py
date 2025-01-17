import random

def numGuesser():
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    print("Type 'exit' to quit the game.")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Prompt the user for input
            user_input = input("Enter your guess: ")

            # Allow the user to exit the game
            if user_input.lower() == "exit":
                print("Thanks for playing! Goodbye!")
                break

            # Convert the input to an integer
            guess = int(user_input)

            # Increment the attempts counter
            attempts += 1

            # Provide feedback
            if guess < target_number:
                print("Higher")
            elif guess > target_number:
                print("Lower")
            else:
                print(f"Congratulations! You've guessed the number {target_number} correctly.")
                print(f"It took you {attempts} attempts.")
                break

        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a number or type 'exit' to quit.")

# Run the game
if __name__ == "__main__":
    numGuesser()

