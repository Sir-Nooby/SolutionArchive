#Problem J1: Speed fines are not fine! - 2012 (SirNooby)
speed_limit = int(input())
recorded_speed = int(input())

difference = recorded_speed - speed_limit

if difference >= 31:
    print("You are speeding and your fine is $500.")
elif difference >= 21:
    print("You are speeding and your fine is $270.")
elif difference >= 1:
    print("You are speeding and your fine is $100.")
else:
    print("Congratulations, you are within the speed limit!")