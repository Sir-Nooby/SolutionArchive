#Problem J2: Rotating Letters - 2013 (SirNooby)
letters = ["I", "O", "S", "H", "Z", "X", "N"]

word = input()

for i in range(len(word)):
    if word[i] not in letters:
        print("NO")
        break
    elif i == len(word)-1:
        print("YES")
