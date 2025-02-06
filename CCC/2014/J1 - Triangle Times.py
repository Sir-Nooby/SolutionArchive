#Problem J1: Triangle Times - 2014 (SirNooby)
sides = []
for i in range(3):
    sides.append(int(input()))

if sum(sides) == 180:
    if sides[0] == sides[1] == sides[2]:
        print("Equilateral")
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")