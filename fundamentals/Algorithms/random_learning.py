class User:
    def __init__(self, name, email_address):
        self.name = "Micah"
        self.email = "wendorfmicah0@gmail.com"
        self.account_balance = 8000

reinhardt = User("Reinhardt Smash", "reinhardt@overwatch.com")
hanzo = User("Hanzo Ninja", "hanzo@overwatch.com")
print(reinhardt.name)
print(hanzo.name)