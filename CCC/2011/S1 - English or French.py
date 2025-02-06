#Problem S1: English or French - 2011 (SirNooby)
lines = int(input())
t = 0
s = 0

for i in range(lines):
    current_line = str(input())
    s += current_line.count("s")
    s += current_line.count("S")
    t += current_line.count("t")
    t += current_line.count("T")

if t > s:
    print("English")
else:
    print("French")