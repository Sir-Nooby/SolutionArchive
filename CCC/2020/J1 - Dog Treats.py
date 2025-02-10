#Problem J1: Dog Treats - 2020 (SirNooby)
small = int(input())
medium = int(input())
large = int(input())
    
total = small + medium*2 + 3*large

if total >= 10:
    print("happy")
else:
    print("sad")