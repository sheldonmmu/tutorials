import random

#introduction

print("You're going to create a story with me. Answer these questions by typing an answer and I'll generate an adventure story.")

#collecting the adventurers name
print("Give me the name of a person:")
name = input()

#generating a random weapon
# creating a list of weapons
weapon_list = ["sword", "hammer", "banana", "axe", "mace"]
 
# using random.randrange() to get a random number
rand_idx = random.randrange(len(weapon_list))
random_weapon = weapon_list[rand_idx]

#collecting a user generated monster
print("Now give me the name of a monster:")
f = input() + 's'
 
# generating random number of enemies
number = random.randint(2,100)

#collecting a user generated emotion
print("Choose an emotion:")
e = input()

#story output
print("Here is your story.")
  
print(name,"found a", random_weapon, "and fought", number, f, ".",
"Afterwards", name, "felt", e, ".")