#Problem J2: Donut Shop - 2025 (SirNooby)
donuts = int(input())

transcations = int(input())

for i in range(transcations):
    symbol = str(input())
    number = int(input())
    if symbol == "+":
        donuts += number
    else:
        donuts -= number

print(donuts)
