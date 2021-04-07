class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            'checkings': BankAccount(int_rate = 0.08, balance = 0),
            'savings': BankAccount(int_rate = 0.04, balance = 0)
        }

    def make_deposit(self, account_type, amount):
        self.account[account_type].deposit(amount)
        return self

    def make_withdrawal(self, account_type, amount):
        self.account[account_type].withdrawal(amount)
        return self

    def display_user_balance(self, account_type):
        print(f"User: {self.name}, {account_type} Balance: {self.account[account_type].balance}")
        return self

    def transfer_money(self, other_user, account_type, amount):
        self.account[account_type].balance -= amount
        other_user.account[account_type].balance += amount
        return self

class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -+ amount
        if(self.balance - amount < 0):
            print("Insufficient funds. Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self


reinhardt = User("Reinhardt", "reinhardt@overwatch.com")
hanzo = User("Hanzo", "hanzo@overwatch.com")

reinhardt.make_deposit('checkings', 1000).display_user_balance('checkings').transfer_money(hanzo, 'checkings', 1000)
hanzo.display_user_balance('checkings')


# hanzo = User("Hanzo", "hanzo@overwatch.com")
# mercy = User("Mercy", "mercy@overwatch.com")


# # 1st user
# reinhardt.make_deposit(1000).make_deposit(500).make_deposit(5000).make_withdrawal(3000).transfer_money(mercy, 1000).display_user_balance()

# # 2nd user
# hanzo.make_deposit(3000).make_deposit(50).make_withdrawal(1025).make_withdrawal(85)

# # 3rd user
# mercy.make_deposit(10000).make_withdrawal(500).make_withdrawal(800).make_withdrawal(1000).display_user_balance()

# checkings = BankAccount()
# savings = BankAccount()

# checkings.deposit(100).deposit(50).deposit(2000).withdrawal(600).yield_interest().display_account_info()
# savings.deposit(5000).deposit(2000).withdrawal(40).withdrawal(60).withdrawal(55).withdrawal(555).yield_interest().display_account_info()