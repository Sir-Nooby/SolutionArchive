#Problem S1: Voronoi Villages - 2018 (SirNooby)
villages = int(input())

village = [int(input()) for i in range(villages)]
village.sort()

lowest = float("inf")

for i in range(len(village)):
    if i == 0 or i == len(village)-1:
        pass
    else:
        total = ((village[i]-village[i-1]) / 2) + ((village[i+1]-village[i]) / 2)
        if total < lowest:
            lowest = total

print(round(lowest, 1))
