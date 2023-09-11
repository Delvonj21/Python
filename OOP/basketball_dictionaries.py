# TODO Challenge 1: Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary
class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    def __repr__(self):
        return f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets",
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics",
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets",
}


# TODO Complete challenge 2: Create 3 instances of the Player class using the given dictionaries

player_kevin = Player(kevin)
print(player_kevin)

player_jason = Player(jason)
print(player_jason)

player_kyrie = Player(kyrie)
print(player_kyrie)


# TODO Complete challenge 3: Populate a new list with Player instances from the list of players.

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {"name": "", "age": 16, "position": "P", "team": "en"},
]

#! for loop over the list of dictionaries
#! each time use that dictionary info
#! to create a new player instances

new_team = []
for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)
