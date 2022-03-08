import os

from art import auction_gavel

print(auction_gavel)

bids = {}

bidding_finish = False


def find_hightest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record {"Name": Number, "Name2": Number2}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finish:

    name = input("What is your name?: ")

    price = int(input("What is your bid?: $"))

    bids[name] = price

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        bidding_finish = True
        find_hightest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
