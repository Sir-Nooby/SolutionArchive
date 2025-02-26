#Problem S1: Positioning Peter's Paintings - 2025 (SirNooby)
a, b, x, y = map(int, input().split())

total1 = (a+x)*2 + (max(b, y))*2
total2 = (b+y)*2 + (max(a, x))*2

print(min(total1, total2))
