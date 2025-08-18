#Problem S2: Bridge Transport - 2013 (SirNooby)
max_weight = int(input())

car_amount = int(input())
bridge = []

weight = 0
total_cars = 0

for i in range(car_amount):
    car = int(input())

    bridge.append(car)
    weight += car

    if len(bridge) > 4:
        weight -= bridge[0]
        bridge.pop(0)
    
    if weight > max_weight:
        break
    else:
        total_cars += 1

print(total_cars)