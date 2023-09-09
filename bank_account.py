class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        # instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        # increases the account balance by the given amount
        self.balance += amount
        return self

    def withdraw(self, amount):
        # If there is sufficient funds
        #  decreases the account balance by the given amount
        if (self.balance - amount) >= 0:
            self.balance -= amount
        # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee"
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        # gives chance to chain methods
        return self

    def display_account_info(self):
        # print to the console: eg. "Balance: $100"
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


checking = BankAccount(0.02, 2000)
savings = BankAccount(0.05, 1000)

checking.deposit(10).deposit(20).deposit(30).withdraw(500)
checking.yield_interest().display_account_info()
print("---------------")
savings.deposit(50).deposit(20).withdraw(50).withdraw(20).withdraw(30).withdraw(200)
savings.yield_interest().display_account_info()
