class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

reinhardt = User("Reinhardt", "reinhardt@overwatch.com")
hanzo = User("Hanzo", "hanzo@overwatch.com")
mercy = User("Mercy", "mercy@overwatch.com")

# 1st user
reinhardt.make_deposit(1000).make_deposit(500).make_deposit(5000).make_withdrawal(3000).transfer_money(mercy, 1000).display_user_balance()

# 2nd user
hanzo.make_deposit(3000).make_deposit(50).make_withdrawal(1025).make_withdrawal(85)

# 3rd user
mercy.make_deposit(10000).make_withdrawal(500).make_withdrawal(800).make_withdrawal(1000).display_user_balance()