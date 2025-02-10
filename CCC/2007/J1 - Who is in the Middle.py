#Problem J1: Who is in the Middle? - 2007 (SirNooby)
bowls = []
for i in range(3):
    bowls.append(int(input()))

bowls.sort()
print(bowls[1])