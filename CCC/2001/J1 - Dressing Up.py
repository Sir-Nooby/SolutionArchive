#Problem J1: Dressing Up - 2001 (SirNooby)
scale = int(input())

length = scale * 2

for i in range(1, scale+1, 2):
    print("*" * i + " " * (length-(i*2)) + "*" * i)

for i in range(scale-2, 0, -2):
    print("*" * i + " " * (length-(i*2)) + "*" * i)
