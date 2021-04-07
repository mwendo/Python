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

reinhardt = User("Reinhardt", "reinhardt@overwatch.com")
hanzo = User("Hanzo", "hanzo@overwatch.com")
mercy = User("Mercy", "mercy@overwatch.com")

reinhardt.make_deposit(1000)
reinhardt.make_deposit(500)
reinhardt.make_deposit(5000)
reinhardt.make_withdrawal(3000)

reinhardt.display_user_balance()