# Spotlight Challenge

"""
green:
  public - 0
  private - maintain speed
  emergency - maintain speed
  human - maintain speed

red:
  public - 0 
  private - 0
  emergency - 20
  human - 0

white:
  public - 30
  private - 0 
  emergency - maintain speed  
  human - 0

yellow:
  public - 0
  private - 20 
  emergency - 30
  human - 0
"""

speed = 25
vehicle_type = "human"
light_color = "green"

if light_color == "green":
  if vehicle_type == "public":
    speed = 0


if light_color == "red":
  if vehicle_type == "emergency":
    speed = 20
  else:
    speed = 0

if light_color == "white":
  if vehicle_type == "private" or vehicle_type == "human":
    speed = 0
  if vehicle_type == "public":
    speed = 30

if light_color == "yellow":
  if vehicle_type == "public" or vehicle_type == "human":
    speed = 0
  elif vehicle_type == "emergency":
    speed = 30
  else:
    speed = 20

print(f"the speed is: {speed}")


