#Problem J2: Chili Peppers - 2023 (SirNooby)
peppers = {
    "Poblano":1500,
    "Mirasol":6000,
    "Serrano":15500,
    "Cayenne":40000,
    "Thai":75000,
    "Habanero":125000
}

pepper_count = int(input())
spiciness = 0

for i in range(pepper_count):
    spiciness += peppers.get(str(input()))

print(spiciness)