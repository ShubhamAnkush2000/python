
#7588944588 Don number

def Addition(No1,No2):
    An = 0
    Ans = No1 + No2
    return Ans

def Substrction(No1,No2):
    An = 0
    Ans = No1 - No2
    return Ans

def main():
    Value1 = int(input("Enter the first number :"))
    Value2 = int(input("Enter the second number :"))
    
    Ret = Addition(Value1,Value2)
    print("Addition is :",Ret)
    
    Ret = Substrction(Value1,Value2)
    print("Substrction is :",Ret)
    
    
if __name__ == "__main__":
    main()