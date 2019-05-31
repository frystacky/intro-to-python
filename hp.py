import random

health = 50

difficulty = 1

if difficulty == 1:
    print("easy mode on")
elif difficulty == 2:
    print("medium mode on")
else:
    print("hard mode on")

potion_hp = int(random.randint(25,50) / difficulty)

health += potion_hp

print("hp is " , health)
