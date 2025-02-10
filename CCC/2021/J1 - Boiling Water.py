#Problem J1: Boiling Water - 2021 (SirNooby)
boil = int(input())
pressure = 5 * boil - 400

print(pressure)

if pressure < 100:
    print("1")
elif pressure > 100:
    print("-1")
else:
    print("0")