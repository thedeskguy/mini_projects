def highest_bidder(bidding_dict):
    winner=""
    highest_bid=0
    for bid in bidding_dict:
        bid_amt=bidding_dict[bid]
        if bid_amt>highest_bid:
            highest_bid=bid_amt
            winner=bid

    print(f"The winner is {winner} with bid of {highest_bid}") 

bids={}
continue_bidding=True
while continue_bidding:
    name=input("What is your name? ")
    price=int(input("What is your bid: $"))
    bids[name]=price
    should_continue=input("Are there any other bidders, Type 'Y' to continue else 'N'\n").lower()
    if should_continue=="n":
        continue_bidding=False
        highest_bidder(bids)
    elif should_continue=="y":
        print("\n"*20)


