#Problem J3: Double Dice - 2014 (SirNooby)
rounds = int(input())

a_points, d_points = 100, 100

for i in range(rounds):
    dice_roll = list(map(int, input().split()))
    if dice_roll[0] > dice_roll[1]:
        d_points -= dice_roll[0]
    elif dice_roll[1] > dice_roll[0]:
        a_points -= dice_roll[1]
    else:
        pass

print(a_points)
print(d_points)