class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited %i to the account of %s" % (amount, self.owner))
        print(f"Your balance: %i" % self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! Cannot withdraw %i from %s's account" % (amount, self.owner))
        else:
            self.balance -= amount
            print(f"Withdrew %i from %s's account" % (amount, self.owner))
            print(f"Your balance: %i" % self.balance)

account = Account("Arsen", 1000000)
account.deposit(200000)
account.withdraw(10000)
account.withdraw(100000000)

