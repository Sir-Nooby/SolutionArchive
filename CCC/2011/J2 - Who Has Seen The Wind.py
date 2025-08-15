#Problem J2: Who Has Seen The Wind - 2011 (SirNooby)
humidity = int(input())
time = int(input())

ground = False

for i in range(1, time+1):
    altitude = -6 * i**4  + humidity * i**3 + 2 * i**2 + i
    if altitude <= 0:
        ground = True
        break

if ground:
    print("The balloon first touches ground at hour:")
    print(i)
else:
    print("The balloon does not touch ground in the given time.")