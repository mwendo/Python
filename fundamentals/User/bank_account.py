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

checkings = BankAccount()
savings = BankAccount()

checkings.deposit(100).deposit(50).deposit(2000).withdrawal(600).yield_interest().display_account_info()
savings.deposit(5000).deposit(2000).withdrawal(40).withdrawal(60).withdrawal(55).withdrawal(555).yield_interest().display_account_info()