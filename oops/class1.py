#!/usr/bin/python
#Filname is class1.py
class Account:

    def __init__(self, name, balance):
         self.name = name
         self.balance = balance
     
    def deposit(self, amount):
        if amount > 0:
           self.balance = self.balance + amount
           print(f'{self.name} balance is {self.balance}')
   
    def  withdraw(self, amount):
        if amount > 0:
           self.balance = self.balance - amount
           print(f'{self.name} balance is {self.balance}')

    def  showbalance(self):
         print(f'{self.name} balance is {self.balance}')

if __name__ == "__main__": 
#   pass   
    skakkar_account = Account('shehbab',100) # object = class(Assign value to constructor)
    skakkar_account.showbalance()   # object.function()
    skakkar_account.deposit(150)   
    skakkar_account.showbalance()
    print(f'{skakkar_account.name}')  #  object.AttributeofClass 
    skakkar_account.withdraw(45)  
    skakkar_account.showbalance()
    print(f'{skakkar_account.balance}')
    skakkar_account.balance = 200
    print(f'{skakkar_account.balance}')
    #del skakkar_account.balance
    print(f'{skakkar_account.balance}')
    print(f'{skakkar_account}')
    #del  skakkar_account
    
    print(f'{skakkar_account}')

    lsoni_account = Account('lokesh',200)
    lsoni_account.deposit(1000)
    print(f'Lokesh balance  = {lsoni_account.balance}')




