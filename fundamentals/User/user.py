class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

reinhardt = User("Reinhardt", "reinhardt@overwatch.com")
hanzo = User("Hanzo", "hanzo@overwatch.com")
mercy = User("Mercy", "mercy@overwatch.com")

# 1st user
reinhardt.make_deposit(1000)
reinhardt.make_deposit(500)
reinhardt.make_deposit(5000)
reinhardt.make_withdrawal(3000)

# 2nd user
hanzo.make_deposit(3000)
hanzo.make_deposit(50)
hanzo.make_withdrawal(1025)
hanzo.make_withdrawal(85)

# 3rd user
mercy.make_deposit(10000)
mercy.make_withdrawal(500)
mercy.make_withdrawal(800)
mercy.make_withdrawal(1000)

reinhardt.transfer_money(mercy, 1000)
reinhardt.display_user_balance()
mercy.display_user_balance()