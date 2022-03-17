# Import modules.
from art import logo, vs
from game_data import data
from random import choice
from os import system, name


def clear():
    """Clear the terminal output."""
    if name == 'nt':
        _ = system('cls')


def check_answers(user_guess, a_followers, b_followers):
    """
    Take the user guess and follower counts and return if they got it right.
    """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


def format_data(compare):
    """Format the account data into printable format."""
    compare_name = compare['name']
    compare_descr = compare['description']
    compare_country = compare['country']
    return f"{compare_name}, a {compare_descr}, from {compare_country}"


# Display the "Higher Lower" logo.
print(logo)
score = 0
game_should_continue = True
compare_b = choice(data)

# Print Comparison A, which is a random person.
# You must display their name, a description, and their country.
while game_should_continue:
    compare_a = compare_b
    compare_b = choice(data)

    while compare_a == compare_b:
        compare_b = choice(data)

    print(f"Compare A: {format_data(compare_a)}.")
    # Print the "VS" logo.
    print(vs)
    # Print Comparison B, which should display the same info as A.
    print(f"Against B: {format_data(compare_b)}.")

    # Ask the user to choose between "A" or "B".
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check the user's input against the follower count of A and B.
    a_follower_count = compare_a['follower_count']
    b_follower_count = compare_b['follower_count']
    is_correct = check_answers(user_guess, a_follower_count, b_follower_count)

    # Clear the screen between each round.
    clear()
    print(logo)
    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
