#Problem J3: Sumac Sequences - 2011 (SirNooby)
start = int(input())
subtract = int(input())

count = 0

while True:
    count += 1
    if subtract >= 0:
        difference = start - subtract
        start = subtract
        subtract -= difference
        subtract, difference = difference, subtract
    else:
        print(count)
        break