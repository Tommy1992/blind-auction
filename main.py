from replit import clear
from art import logo

print(logo)
bidders_and_bid = {}
new_bids = True
highest_bid = 0
highest_bidder = ""

while new_bids == True:
    name = input("Your name is? ")
    bid = input("What is your bid? ")
    bidders_and_bid[name] = bid
    print(bidders_and_bid)
    clear()
    more_bidders = input(
        "Anyone else who want to bid? Type in yes or no, pls.")
    if more_bidders == "no":
        new_bids = False
        for single_bid in bidders_and_bid:
            if int(bidders_and_bid[single_bid]) > highest_bid:
                highest_bidder = bidders_and_bid[single_bid]
        print(
            f"The highest bidder is {single_bid} with the bid of: {highest_bidder} €."
        )
