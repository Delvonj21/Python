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
      print (f"First Name: {self.first_name}")
      print (f"Last Name: {self.last_name}")
      print (f"Email: {self.email}")
      print (f"Age: {self.age}")
      print (f"Rewards Member: {self.is_rewards_member}")
      print (f"Gold Card Points: {self.gold_card_points}")
      print("---------------------------------")
    
    
  # enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

  def enroll(self):
      self.is_rewards_member = True
      self.gold_card_points = 200
  
  # spend_points(self, amount) - have this method decrease the user's points by the amount specified.
  def spend_points(self, amount):
      self.gold_card_points -= amount

my_user = User("Delvon", "Johnson", "codingdojo@email.com", "99")
user1 = User("Jane", "Hubey", "Jana@email.com", "2")
user2 = User("Barbara", "Johnson", "Barb@email.com", "10")
my_user.enroll()
my_user.spend_points(50)
user2.enroll()
user2.spend_points(80)
my_user.display_info()
user1.display_info()
user2.display_info()


  