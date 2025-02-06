#Problem J2: Vote Count - 2014 (SirNooby)
votes = int(input())
people = str(input())

if people.count("A") > people.count("B"):
    print("A")
elif people.count("B") > people.count("A"):
    print("B")
else:
    print("Tie")