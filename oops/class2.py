#!/usr/bin/python
#Filname is class1.py
class Account:

    def __init__(self, name, balance):
         self.name = name
         self.balance = balance
    def deposit(self, amount):
        if amount > 0:
           self.balance = self.balance + amount
           self.showbalance()
    def  withdraw(self, amount):
        if self.balance >= amount > 0:
           self.balance = self.balance - amount
           self.showbalance()
        else:
           print(f'Your balance {self.balance} is less than amount {amount} withdrawn')
    
    def  showbalance(self):
         print(f'{self.name} balance is {self.balance}')

if __name__ == "__main__": 
#   pass   
    skakkar_account = Account('shehbab',100) # object = class(Assign value to constructor)
    skakkar_account.deposit(150)   
    skakkar_account.showbalance()
    skakkar_account.withdraw(445)  
    skakkar_account.showbalance()
    lsoni_account = Account('lokesh',200)
    lsoni_account.deposit(1000)
    print(f'Lokesh balance  = {lsoni_account.balance}')
