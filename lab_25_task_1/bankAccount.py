class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит на суму {amount} успішно зараховано.")
        else:
            print("Сума депозиту має бути більшою за 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} успішно знято з вашого рахунку.")
        else:
            print("Недостатньо коштів на рахунку або сума зняття некоректна.")


