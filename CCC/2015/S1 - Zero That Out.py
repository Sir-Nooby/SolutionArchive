#Problem S1: Zero That Out - 2015 (SirNooby)
integer = []

numbers = int(input())

for i in range(numbers):
    order = int(input())
    if order == 0:
        integer.pop(-1)
    elif order != 0:
        integer.append(order)

if len(integer) == 0:
    integer.append("0")

print(sum(integer))