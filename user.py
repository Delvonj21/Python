# For this assignment you will create the user class and add a couple methods!

# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        # Also include default attributes:
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Methods:
    # display_info(self) - Have this method print all of the users' details on separate lines.

    def display_info(self):
        print("---------------------------------")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("---------------------------------")

    # enroll(self) - Print user already a member

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return self

            # Have this method change the user's member status to True
        self.is_rewards_member = True
        # set their gold card points to 200
        self.gold_card_points = 200

        return self

    # spend_points(self, amount)
    # make sure they have enough points, return a error message if they don't
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Insufficient Points!")
            return False

        # have this method decrease the user's points by the amount specified.
        self.gold_card_points -= amount


my_user = User("Delvon", "Johnson", "dj@codingdojo.com", 34)
my_user.display_info()

user2 = User("Jana", "Hubey", "jane@codingdojo.com", 25)
user3 = User("Barbara", "Johnson", "barb@codingdojo.com", 99)

my_user.spend_points(50)
user2.enroll().spend_points(80)

my_user.display_info()
user2.display_info()
user3.display_info()
