class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", amount)

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

acc = BankAccount("Pratiksha", 5000)

acc.display()
acc.deposit(2000)
acc.withdraw(1000)
acc.display()