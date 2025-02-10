#Problem J2: Time to Decompress - 2019 (SirNooby)
lines = int(input())

codes = []
for i in range(lines):
    code = str(input()).replace(" ", "")
    codes.append(code)
    
for i in codes:    
    print(i[-1] * int(i[0:len(i)-1]))
