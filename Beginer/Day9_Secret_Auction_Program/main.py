import os
import art

os.system("cls")
print(art.logo)
bid_dict = {}
def main_loop():
    continue_biding = "yes"
    while continue_biding == "yes":
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        continue_biding = input("Are there any other bidders? (yes/no): ")
        bid_dict[name] = bid
        os.system("cls")


print("Welcome to the secret auction program.")
main_loop()
print(bid_dict)
name_of_highest_bidder = ""
highest_bid = 0
for name, bid in bid_dict.items():
    if bid > highest_bid:
        highest_bid = bid
        name_of_highest_bidder = name
print(f"The highest bid is {highest_bid} for {name}.")

