#Problem J1: Telemarketer or Not? - 2018 (SirNooby)
number = []

for i in range(4):
    number.append(int(input()))


if number[0] == 8 or number[0] == 9:
    if number[1] == number[2]:
        if number[3] == 8 or number[3] == 9:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")