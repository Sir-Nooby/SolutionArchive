#Problem J2: Sounds Fishy! - 2012 (SirNooby)
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b < c < d:
    print("Fish Riving")
elif a > b > c > d:
    print("Fish Diving")
elif a == b == c == d:
    print("Fish At Constant Depth")
else:
    print("No Fish")