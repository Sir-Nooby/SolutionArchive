#Problem S1: Sum Game - 2017 (SirNooby)
runs = int(input())

swifts = input().split()
semas = input().split()

swift_total = 0
semas_total = 0

total = 0

for i in range(runs):
    swift_total += int(swifts[i])
    semas_total += int(semas[i])
    
    if swift_total == semas_total:
        total = i + 1

print(total)
