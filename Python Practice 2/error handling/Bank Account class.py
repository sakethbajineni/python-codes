class BankAccount:
    def __init__(self,account_number):
        self.account_number=str(account_number)
        self.balance=0
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            raise ValueError("Insuffient Funds")
            # print("Insufficient funds")
    def deposit(self,amount):
        self.balance+=amount
    def get_balance(self):
        return self.balance
def transef_amount(acc_1,acc_2,amount):
    try:
        acc_1.withdraw(amount)
        acc_2.deposit(amount)
        return  True
    except:
        return False

user_1=BankAccount("001")
user_2=BankAccount("002")
user_1.deposit(250)
user_2.deposit(100)
print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))
print(transef_amount(user_1,user_2,50))
print("transferring 50/- from user_1 to user_2")
print("User 1 Balance: {}/-".format(user_1.get_balance()))
print("User 2 Balance: {}/-".format(user_2.get_balance()))



