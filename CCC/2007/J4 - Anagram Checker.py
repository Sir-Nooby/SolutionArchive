#Problem J4: Anagram Checker - 2007 (SirNooby)
x = sorted(input().replace(" ", ""))
y = sorted(input().replace(" ", ""))

if x == y:
    print("Is an anagram.")
else:
    print("Is not an anagram.")