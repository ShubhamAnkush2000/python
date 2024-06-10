
class HDFC:
    ROI = 9.5
    
    def __init__(self,Name,Amount):
        self.AccountHolder = Name
        self.Balance = Amount
        print("Welcome ",self.AccountHolder)
        print("Account get succesfully created with initial balance :",self.Balance)
              
    def DisplayBalance(self):
        print("Hello",self.AccountHolder)
        print("Your acount balance is :",self.Balance)
    
    @classmethod 
    def DisplayBankInfo(cls):
        print("welcome to HDFC bank portal")
        print("our bank is PVT LTD bank")
        print("We provide the Rate of Interest on saving Account is",cls.ROI) 
        
    @staticmethod
    def DisplayKycInfo():
        print("According to the rules of rbi you should provide below docments for Kyc")
        print("your Aadhar Card")
        print("your Pan card")
        print("your passport size photo")
              
    def DisplayBalance(self):
        print("Your account balance is :",self.Balance)
        
    def Withdraw(self,Amount):
        if self.Balance < Amount:
            print("There is on sufficient balance")
        else:
            self.Balance =self.Balance-Amount
            print("Amount withdawal succesfully...")
    
    def Deposit(self,Amount):
        self.Balance = self.Balance + Amount
        print("Amount deposited seccesfully...")


def main():
    
    print("ROI of HDFC BAnk is :",HDFC.ROI)
    
    HDFC.DisplayBankInfo()
    HDFC.DisplayKycInfo()
    
    print("Createing NEW Account...")
    Amit = HDFC("Amit",5000)
    
    print("Createing NEW Account...")
    Sagar = HDFC("Sagar",3000)
    
    print("PERforming operation on Amit")
    Amit.Deposit(2000)
    Amit.DisplayBalance()
    
    Amit.Withdraw(1000)
    Amit.DisplayBalance()
    
    print("performing operation on Sagar Account")
    Sagar.Deposit(4000)
    Sagar.DisplayBalance()
    
    Sagar.Withdraw(500)
    Sagar.DisplayBalance()
    
if __name__ == "__main__":
    main()