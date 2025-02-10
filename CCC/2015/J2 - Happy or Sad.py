#Problem J2: Happy or Sad - 2015 (SirNooby)
text = str(input())

happy = text.count(":-)")
sad = text.count(":-(")

if happy == 0 and sad == 0:
    print("none")
elif sad > happy:
    print("sad")
elif happy > sad:
    print("happy")
else:
    print("unsure")