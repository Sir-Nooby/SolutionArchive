#Problem J2: Dusa and the Yobis - 2024 (SirNooby)
dusa = int(input())

while True:
    yobi = int(input())
    if dusa > yobi:
        dusa += yobi
    else:
        print(dusa)
        break
