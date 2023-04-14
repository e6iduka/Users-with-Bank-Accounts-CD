class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.intRate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.checkBalance(amount):
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def checkBalance(self, amount):
        if(self.balance < amount):
            print(f"You don't have enough money. Balance: {self.balance}")
            return False
        else:
            return True

    def displayAccountInfo(self):
        print(f"Balance: ${self.balance:.2f}")
        return self

    def yieldInterest(self):
        if(self.balance > 0):
            self.balance *= 1+ self.intRate
        return self

    def __repr__(self):
        return f"Balance: {self.balance:.2f} Interest Rate: {self.intRate}"

class User:
    def __init__(self,name, bank="Chase"):
        self.name = name
        self.bankAccount = {bank:BankAccount(.02,100)}
    
    def addBank(self, interest, startBalance, name):
        self.bankAccount[name] = BankAccount(interest, startBalance)
        return self

    def makeDeposit(self,amount, bank):
        self.bankAccount[bank].deposit(amount)
        return self

    def makeWithdrawal(self,amount, bank):
        self.bankAccount[bank].withdraw(amount)
        return self

    def displayBalance(self, bank):
        self.bankAccount[bank].displayAccountInfo()
        return self




jim = User("Jim")
jim.makeDeposit(100, "Chase").makeDeposit(500, "Chase").makeDeposit(20, "Chase").displayBalance("Chase")

dwight = User("Dwight")
dwight.makeDeposit(10, "Chase").makeDeposit(1000, "Chase").makeWithdrawal(500, "Chase").displayBalance("Chase")

pam = User("Pam")
pam.makeDeposit(400, "Chase").makeWithdrawal(10, "Chase").makeWithdrawal(50, "Chase").makeWithdrawal(30, "Chase").displayBalance("Chase")
pam.addBank(.05, 100, "WellsFargo")
pam.displayBalance("WellsFargo")