#Problem J2: Roll the Dice - 2006 (SirNooby)
dice1 = int(input())
dice2 = int(input())

total = 0

for i in range(1, dice1+1):
    for v in range(1, dice2+1):
        if i + v == 10:
            total += 1

if total != 1:
    print("There are " + str(total) + " ways to get the sum 10.")
else:
    print("There is " + str(total) +  " way to get the sum 10.")