class MyAccount(object):

    #class attribute
    DeAccountNnumber = 1

    #instance attribute
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        self.accountNumber = MyAccount.DeAccountNnumber
        MyAccount.DeAccountNnumber = MyAccount.DeAccountNnumber + 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance < amount:
            print("Your account balance is less.")         
        else:
            self.balance -= amount

    def actualBalance(self):
        return self.balance

# #object instantiation
if __name__ == '__main__':
    obj = MyAccount('onderi', 2000)
    obj.deposit(10000)
    print(obj.actualBalance())
    obj.withdraw(2000)
    print(obj.actualBalance())
