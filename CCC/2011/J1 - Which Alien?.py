#Problem J1: Which Alien? - 2011 (SirNooby)

ant = int(input())
eyes = int(input())

if ant >= 3 and eyes <= 4:
    print("TroyMartian")
    
if ant <= 6 and eyes >= 2:
    print("VladSaturnian")

if ant <= 2 and eyes <= 3:
    print("GraemeMercurian")
