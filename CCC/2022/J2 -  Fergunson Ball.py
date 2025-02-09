#Problem J2: Fergunsonball - 2022 (SirNooby)
players = int(input())

star_players = 0

for i in range(players):
    points = int(input())
    fouls = int(input())
    total = 5*points-3*fouls
    if total > 40:
        star_players +=1

if star_players == players:
    print(str(star_players) + "+")
else:
    print(star_players)
    