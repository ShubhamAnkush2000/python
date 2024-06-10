from functools import reduce

def CheakEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False
def Increase(No):
    return No + 2

def Add(A,B):
    return A+B

def main():
    Data = []
    print("Enter number of element :")
    Size = int(input())
    
    print("enter the element :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    output = list(filter(CheakEven,Data))
    print(output)
    
    moutput = list(map(Increase,output))
    print(moutput)
    
    result = reduce(Add, moutput)
    print(result)
           
if __name__ == "__main__":
    main()