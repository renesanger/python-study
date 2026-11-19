import random

random_number = 0

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    random_number = random.randint(1, 6)
    return random_number

print(get_random_dice_roll())
print(random_number)
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())