from art import logo
from random import randint

EASY_LVL_TURNS = 10
HARD_LVL_TURNS = 5


# Get ASCII logo printed when game starts.
print(logo)

# Function to check the user's guess against actual answer.


def check_answer(guess, answer, turns):
    """Check answer against guess, return the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}!")

# Make function to set difficulty.


def check_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LVL_TURNS
    if level == 'hard':
        return HARD_LVL_TURNS


def random_number():
    """Return random number between 1 and 100."""
    number = randint(1, 100)
    return number


def game():
    # Choosing a number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random_number()
    print(f"Psst, the correct answer is {answer}.")
    # Let the user guess a number.
    turns = check_difficulty()
    guess = 0
    # Repeat the guessing functionality if they get it wrong.
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess again.")


game()
