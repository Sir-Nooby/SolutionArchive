#Problem S1: Crazy Fencing - 2021 (SirNooby)
pieces = int(input())

heights = list(map(int, input().split()))

widths = list(map(int, input().split()))

total = 0

for i in range(pieces):
    total += (0.5 * widths[i] * (heights[i+1]+heights[i]))
print(total)
