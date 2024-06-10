
def Marvellous(Value1,Value2):
    Addition = Value1 + Value2
    substraction = Value1 - Value2
    Multiplication = Value1 * Value2
    
    return Addition,substraction,Multiplication
   

def main():
    Ret = Marvellous(11,6)
    print("Addition is :",Ret[0])
    print("sub is :",Ret[1])
    print("multi is :",Ret[2])
      
if __name__ == "__main__":
    main() 