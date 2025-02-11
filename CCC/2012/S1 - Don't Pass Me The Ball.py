#Problem S1: Don't Pass Me The Ball! - 2012 (SirNooby)
import math

player = int(input())

if player < 4:
    print(0)
else:
    print(math.factorial(player-1)//(3*math.factorial(player-4)) //2)
