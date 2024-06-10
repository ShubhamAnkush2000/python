
def Marvellous(Value1,Value2):
    Addition = Value1 + Value2
    substraction = Value1 - Value2
    Multiplication = Value1 * Value2
    
    return Addition,substraction,Multiplication
   

def main():
    Ret1,Ret2,Ret3 = Marvellous(11,6)
    print("Addition is :",Ret1)
    print("sub is :",Ret2)
    print("multi is :",Ret3)
      
if __name__ == "__main__":
    main() 