# from replit import clear
from art import logo
import os

print(logo)

new_entry = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {'felipe': 123, 'victoria': 333}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    new_entry[name] = price
    should_continue = input(
        ("Are there any other bidders? Type 'yes' or 'no'.\n"))
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(new_entry)
    elif should_continue == 'yes':
        os.system('cls')
