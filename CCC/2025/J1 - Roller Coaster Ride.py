#Problem J1: Roller Coaster Ride - 2025 (SirNooby)
line_place = int(input())
cars = int(input())
capacity = int(input())

if line_place - (cars * capacity) <= 0:
    print("yes")
else:
    print("no")
