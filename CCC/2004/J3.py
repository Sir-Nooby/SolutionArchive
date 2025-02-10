#Problem J3: Smile with Similes - 2004 (SirNooby)
adj_count = int(input())
noun_count = int(input())
adj = [str(input()) for i in range(adj_count)]
noun = [str(input()) for i in range(noun_count)]

for i in adj:
    for v in noun:
        print(i + " as " + v)