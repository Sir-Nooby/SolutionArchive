#Problem J3: Deal or No Deal Calculator - 2007 (SirNooby)
cases = int(input())

values = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

chosen = 0
total = 0

for i in range(cases):
    chosen += values[int(input()) - 1]
    
deal = int(input())

total = sum(values) - chosen

if deal >= (total // (10-cases)):
    print("deal")
else:
    print("no deal")