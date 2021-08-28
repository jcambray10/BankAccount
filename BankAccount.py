class BankAccount:
    def __init__(self, rate, balance):
        self.int_rate = (rate * 0.01)
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            interest_yielded = self.balance * self.int_rate
            self.balance += interest_yielded
        return self

BucksFan = BankAccount(0.25, 0)
Catalan = BankAccount(0.3, 0)

BucksFan.deposit(100).deposit(25).deposit(25).withdraw(25).yield_interest().display_account_info()
Catalan.deposit(200).deposit(50).withdraw(20).withdraw(50).withdraw(20).withdraw(50).yield_interest().display_account_info()

# python BankAccount.py 

# echo "# BankAccount" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jcambray10/BankAccount.git
# git push -u origin main
