import random
import os
from art import logo
# Deal the user and computer two cards each with deal_card().


def deal_card():
    """Return random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Create a calculate_score() function that takes a list of cards as input
# and returns the score.


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check for an ace and if total score is higher or lesser than 21.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Create function that provides the result of the game.


def compare(user_score, computer_score):
    """Compare scores and provides a result."""
    # Bug fix if both the user and the computer are over and you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!"

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win, you got a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

# Create play_game() function that will allow the user to play as many times
# as he or she wants.


def play_game():
    """Initiate a BlackJack game"""
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal both the user and the computer two cards using deal_card().
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Call calculate_score() and check for a blackjack in the user or the
    # computer's hand. If the user's score is over 21, then it's game over.

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        # If game goes on, ask the user if he or she wants to draw another
        # card. If yes, draw card with the deal_card() function; if not,
        # end the game.
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n'"
                                     + " to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Let computer draw cards as long as score is under 17 and
    # it didn't get a blackjack.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card)
        computer_score = calculate_score(computer_cards)
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards},"
          " final score: {computer_score}")
    print(compare(user_score, computer_score))

# Ask the user if he or she wants to restart the game. If the answer is 'yes',
# clear the console and start a new game, showing the logo imported from the
# art.py module.


while input("Do you want to play a game of Blackjack? " +
            "Type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_game()
