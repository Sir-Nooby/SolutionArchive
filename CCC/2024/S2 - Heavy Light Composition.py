#Problem S2: Heavy Light Compostion - 2024 (SirNooby)

lines, chars = map(int, input().split())

order = []

for i in range(lines):
    text = input()
    for v in range(chars):
        if text.count(text[v]) > 1:
            order.append("H")
        else:
            order.append("L")

    for x in range(len(order)):
        if x == (len(order) - 1):
            print("T")
            break
        if order[x+1] != order[x]:
            pass
        else:
            print("F")
            break
    order.clear()