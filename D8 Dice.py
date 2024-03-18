D8 = range(1,8)
import random
roll = input ("Type 'roll' to roll the dice:")
if roll == "roll":
    print(random.choice(D8))