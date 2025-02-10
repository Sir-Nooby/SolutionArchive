#Problem J2: Epidemiology - 2020 (SirNooby)
days = 0

total = int(input())
start = int(input())
rate = int(input())

infected = start

while total >= infected:
    infected += start * rate
    start = start * rate
    days += 1

print(days)