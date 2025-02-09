#Problem J1: Deliv-e-droid - 2023 (SirNooby)
packages = int(input())
collisions = int(input())

final = (packages * 50) - (collisions * 10)

if packages > collisions:
    print(final + 500)
else:
    print(final)