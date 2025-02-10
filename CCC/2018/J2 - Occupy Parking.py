#Problem J2: Occupy Parking - 2018 (SirNooby)
cars = int(input())

row_1 = str(input())
row_2 = str(input())

count = 0

for i in range(cars):
    if row_1[i] == "C" == row_2[i]:
        count += 1

print(count)