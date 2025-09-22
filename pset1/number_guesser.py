import random

def number_guesser():
    number = random.randint(1, 1000)
    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 1000 (type 'bye' or 'exit' to quit): ")

        if guess in ["bye", "exit"]:
            break

        if not guess.isdigit():
            print("Please enter a valid number")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number! You took {attempts} attempts!")
            number = random.randint(1, 1000)
            attempts = 0

if __name__ == "__main__":
    number_guesser()
