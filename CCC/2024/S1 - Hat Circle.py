#Problem S1: Hat Circle - 2024 (SirNooby)
people = int(input())

hats = [int(input()) for i in range(people)]

center = (people // 2)

total = 0

for i in range(people // 2):
    if hats[i] == hats[center+i]:
        total += 2

print(total)
