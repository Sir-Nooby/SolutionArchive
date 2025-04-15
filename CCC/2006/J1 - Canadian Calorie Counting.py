#Problem J1: Canadian Calorie Counting - 2006 (SirNooby)
burger = [461, 431, 420, 0]
drink = [130, 160, 118, 0]
sides = [100, 57, 70, 0]
dessert = [167, 266, 75, 0]

total = 0

total += burger[int(input())-1]
total += sides[int(input())-1]
total += drink[int(input())-1]
total += dessert[int(input())-1]

print("Your total Calorie count is {total}.".format(total=total))
