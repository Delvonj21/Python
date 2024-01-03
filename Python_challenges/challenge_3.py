"""
- Use your code from the last lesson or starter code below
- add the follwoing commands
  quit - Quits the game
  menu - display the menu
  walk - PASS
  play - PASS
  feed - PASS
  sleep - PASS
  do trick - PASS
  walk - PASS
  switch - PASS
- any other commands should return the "Invalid Command"
- use a tuple to store menu
"""

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

while is_active:
  command = input("\ncommand-> ")

  if command == "quit":
    is_active = False

  elif command == "menu":
    print("\nMenu:\n")
    for menu_item in MENU:
      print(f" {menu_item} ")

  elif command == "walk":
    pass

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

print("Have A Nice Day!")


