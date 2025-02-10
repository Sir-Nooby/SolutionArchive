#Problem J2: Shifty Sum - 2017 (SirNooby)
number = int(input())
shift = int(input())

total = number

for i in range(1, shift+1):
    total += int(str(number) + "0" * i)

print(total)