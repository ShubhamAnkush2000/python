
def Add(A,B):
    return A+B

def sub(A,B):
    return A-B
      
def Marvellous(Value1,Value2):
    Ans = Add(Value1,Value2)
    print("Add is :",Ans)
    Ans = sub(Value1,Value2)
    print("sub is :",Ans)
   

def main():
    Marvellous(11,7)
   
if __name__ == "__main__":
    main() 