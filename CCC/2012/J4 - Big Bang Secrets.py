#Problem J4: Big Bang Secrets - 2012 (SirNooby)
k = int(input())
word = str(input())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
final_word = ""

for pos in range(len(word)):
    key = 3 * (pos+1) + k
    current = alphabet.find(word[pos])
    total = current - key
    if total < -26:
        total = total // 26
    final_word += alphabet[total]
print(final_word)