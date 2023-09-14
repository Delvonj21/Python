# For this assignment you will create the user class and add a couple methods!

# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

class User:
  def __init__(self, first_name, last_name, email, age):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    self.is_rewards_member = False
    self.gold_card_points = 0

# Methods:
#  - Have this method print all of the users' details on separate lines.
  def display_info(self):
    print("---------------------")
    print(self.first_name)
    print(self.last_name)
    print(self.email)
    print(self.age)
    print(self.is_rewards_member)
    print(self.gold_card_points)
    print("---------------------")

    return self


  
# Have this method change the user's member status to True and set their gold card points to 200.
# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
  def enroll(self):
    if self.is_rewards_member:
      print("User already a member")
      return self
    
    self.is_rewards_member = True
    self.gold_card_points = 200
    return self
    
# Have this method decrease the user's points by the amount specified.
  def spend_points(self, amount):
    if self.gold_card_points < amount:
      print("Insufficient Funds")
      return self
    
      self.gold_card_points -= amount
      return self
      


my_user = User("Delvon", "Johnson", "Dj@codingdojo.com", 69)
his_user = User("Craig", "Johnson", "Cj@codingdojo.com", 99)
her_user = User("Barbara", "Johnson", "Bj@codingdojo.com", 89)

# my_user.display_info()
# my_user.enroll()
# my_user.display_info()
# my_user.spend_points(50)
# his_user.enroll()
# his_user.spend_points(80)
# my_user.enroll()
# my_user.display_info()
# his_user.display_info()
# her_user.display_info()

my_user.enroll().spend_points(50)
my_user.display_info()
his_user.enroll().spend_points(80)
his_user.display_info()
her_user.display_info()



