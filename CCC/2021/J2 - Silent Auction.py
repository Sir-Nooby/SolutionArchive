#Problem J2: Silent Auction - 2021 (SirNooby)
people = int(input())
bidders = []
amount = []

for i in range(people):
    bidders.append(str(input()))
    amount.append(int(input()))

print(bidders[amount.index(max(amount))])