import random

def walk(pet):
  #put your code here
  if current_pet['energy'] < 30:
    print("Too tired to walk.")
    current_pet['energy'] -= random.randint(1, 2)
    current_pet['happiness'] -= random.randint(1, 2)
    return 
  

  gained_happiness = random.randint(1, 4)
  current_pet['happiness'] += gained_happiness
  print(f"You took {current_pet['name']} for a walk. Your pet gained {gained_happiness} happiness and now has {current_pet['happiness']} happiness.")


current_pet = {
  'name': "Buddy",
  'type': "Bardakook",
  'trick': "play fetch",
  'happiness': 100,
  'energy': 100,  
}

MENU = {
  "quit",
  "menu",
  "walk",  
  "play",
  "feed",
  "sleep",
  "do trick",
  "walk",
  "switch",
}

is_active = True
dead = is_active 

while is_active:

  print(f"""
      \n {current_pet['name']} is a {current_pet['type']} that likes to {current_pet['trick']}.
      \n They have {current_pet['happiness']} happiness and {current_pet['energy']} energy. 
""")
  command = input("\ncommand-> ")

  if command == "quit":
    is_active = False

  elif command == "menu":
    print("\nMenu:\n")
    for menu_item in MENU:
      print(f" {menu_item} ")

  elif command == "walk":
    walk(current_pet)

  elif command == "play":
    pass

  elif command == "feed":
    pass

  elif command == "sleep":
    pass

  elif command == "do trick":
    pass

  elif command == "walk":
    pass

  elif command == "switch":
    pass

  else:
    print("Invalid Command")

  #check if pet has died
  if dead:
    is_active = False

print("Have A Nice Day!")