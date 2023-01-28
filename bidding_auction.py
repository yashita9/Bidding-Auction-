import clear

bids = {}
bidding_fininsed = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# 1. The function find_highest_bidder() takes in a dictionary of bidders and their bids.
# 2. It then loops through the dictionary and finds the highest bid.
# 3. It then finds the bidder with the highest bid and returns that bidder’s name.


while not bidding_fininsed:
    name = input("What is your name?: ")
    price = int(input("What is your bid amount?: $"))
    bids[name] = price
    should_continue = input("Are ther any other bidders? Type yes or no. \n")
    if should_continue == "no":
        bidding_fininsed = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
