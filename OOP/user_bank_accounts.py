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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    # Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    # Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self):
        self.account.display_account_info()
        return self


# User test
user1 = User("Delvon", "DJ@codingdojo.com")
user1.make_deposit(100).make_deposit(200).display_user_balance()

user2 = User("Jane", "Jane@codingdojo.com")
user2.make_deposit(1000).display_user_balance().make_withdrawal(200)
user2.display_user_balance()
