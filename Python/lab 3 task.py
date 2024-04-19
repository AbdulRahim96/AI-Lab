# Task 1
class Bank:
    name = "Meezan"

    def Depoit(this, val): #overwriting
        this.name += val
        print("Bank name is ", this.name)

class Account(Bank):
    __accountNumber = 123
    accountType = "Current"
    __balance = 0

    def __init__(this, num):
        this.accountNumber = num


    def Depoit(this, val=0): # overloading
        if(val==0):
            print("No value assigned")
            return
        this.__balance += val
        print("Deposited. Balance is ", this.__balance)

    def Withdraw(this, val):
        if(val > this.__balance):
            print("insuficient funds")
        else:
            this.balance -= val
            print("Withdrawn. Balance is ", this.__balance)

obj = Account(12345)
obj.Depoit(10000)

obj = Bank()
obj.Depoit("UBL")
    