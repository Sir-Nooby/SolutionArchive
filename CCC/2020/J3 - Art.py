#Problem J3: Art - 2020 (SirNooby)
drops = int(input())

x_coordinates = []
y_coordinates = []

for i in range(drops):
    x, y = map(int, input().split(","))
    if 0 <= x < 100 and 0 <= y < 100:
        x_coordinates.append(x)
        y_coordinates.append(y)

lowest = "{a},{b}".format(a=min(x_coordinates)-1, b=min(y_coordinates)-1)
highest = "{a},{b}".format(a=max(x_coordinates)+1, b=max(y_coordinates)+1)

print(lowest)
print(highest)