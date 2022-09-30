class BankAccount:
    accounts=[]
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        return self
        # your code here
    def withdraw(self, amount):
        self.balance-=amount
        return self
        # your code here
    def display_account_info(self):
        print("Balance:",self.balance)
        return self
        # your code here
    def yield_interest(self):
        self.balance=self.balance*self.int_rate+self.balance
        return self
        # your code here
    @classmethod
    def showall(cls):
        for account in cls.accounts:
            account.display_account_info()
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount(0.05,5000),BankAccount(0.05,10000)]
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info()
    def user_allaccounts(self):
        for account in self.account:
            print(account.showall())


account1=BankAccount(0.05,5000)
account2=BankAccount(0.07,10000)
account1.deposit(50).deposit(70).deposit(200).withdraw(100).yield_interest().display_account_info() 
account2.deposit(550).deposit(200).withdraw(13).withdraw(520).withdraw(100).withdraw(70).yield_interest().display_account_info() 
BankAccount.showall() 
Juan=User('Juan','juansdaf@gamil.com')
