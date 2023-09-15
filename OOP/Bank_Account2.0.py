class BankAccount:
  def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

        
  def deposit(self, amount):
      self.balance += amount
      return self
        
  def withdraw(self, amount):
      if self.balance < amount:
          print("Insufficient funds: Charging a $5 fee")
          self.balance -= 5
          return self
      
      self.balance -= amount 
      return self
       
  def display_account_info(self):
      print(f"Balance: {self.balance}")
      return self
        
  def yield_interest(self):
      if self.balance > 0:
          self.balance = (self.balance * self.int_rate)
          return self
      
user1 = BankAccount(0.5, 1000)
user2 = BankAccount(0.4, 5000)


user1.deposit(100).deposit(50).deposit(50).withdraw(500).yield_interest().display_account_info()
user2.deposit(50).deposit(20).withdraw(100).withdraw(200).withdraw(500).withdraw(20).yield_interest().display_account_info()    
 

