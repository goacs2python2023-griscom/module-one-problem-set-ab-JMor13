import random

def dice_roll():
    roll_one = random.randint(1,6)
    roll_two = random.randint(1,6)
    if roll_one + roll_two == 6 or roll_one + roll_two == 7 or roll_one + roll_two == 8:
        return "win"
    else:
        return "lose"

print(dice_roll())