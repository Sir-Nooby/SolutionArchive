#Problem J3: Secret Instructions - 2021 (SirNooby)
last_direction = ""

while True:
    code = str(input())
    if code == "99999":
        break
    instruction = int(code[0]) + int(code[1])
    if instruction == 0:
        print(last_direction + " " + code[2:])
    if instruction % 2 == 0:
        print("right " + code[2:])
        last_direction = "right"
    elif instruction % 2 != 0:
        print("left " + code[2:])
        last_direction = "left"