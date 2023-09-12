from ninja import *
from pet import *

# TODO NINJA BONUS: Use modules to separate out the classes into different files.

black_ninja = Ninja(
    "Delvon",
    "Johnson",
    dog,
    ["cookies", "pie", "doughnuts"],
    ["Burgers", "Chicken", "Sausage"],
)
black_ninja.feed()
black_ninja.walk()
black_ninja.bathe()

print(black_ninja.pet.name)
