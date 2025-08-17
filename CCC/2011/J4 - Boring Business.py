#Problem J4: Boring Business - 2011 (SirNooby)
tiles = [[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4], [3, -5], [4, -5], [5, -5], [5, -4], [5, -3], [6, -3], [7, -3], [7, -4], [7, -5], [7, -6], [7, -7], [6, -7], [5, -7], [4, -7], [3, -7], [2, -7], [1, -7], [0, -7], [-1, -7], [-1, -6]]

position = [-1, -5]

safe = True

while True:
    direction, moves = list(map(str, input().split()))

    if direction == "q":
        break

    for i in range(int(moves)):
        
        if direction == "l":
            position[0] -= 1
        elif direction == "r":
            position[0] += 1
        elif direction == "d":
            position[1] -= 1
        elif direction == "u":
            position[1] += 1

        if position in tiles:
            safe = False
        else:
            tiles.append([position[0], position[1]])

    if safe:
        print(str(position[0]) + " " + str(position[1]) + " " + "safe")
    else:
        print(str(position[0]) + " " + str(position[1]) + " " + "DANGER")
        break