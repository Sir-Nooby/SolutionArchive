#Problem J3: Cold Compress - 2019 (SirNooby)
lines = int(input())

for i in range(lines):
    message = input()
    length = len(message)
    current = 0
    decoded = ""
    
    while current < length:
        count = 0
        symbol = message[current]
        for v in range(current, length):
            if message[v] != symbol:
                break
            count += 1
        decoded += str(count) + " " + symbol + " "
        current += count
    print(decoded)