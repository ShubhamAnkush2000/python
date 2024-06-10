from functools import reduce

CheakEven = lambda No: (No % 2 == 0)
Increase = lambda No : No+2   
Add =lambda A,B:A+B

def filterX(Task,Elements):
    Result = []
    for no in Elements:
        if(Task(no)== True):
            Result.append(no)
    return Result
        
def mapX(Task,Elements):
    Result = []
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result
    
def main():
    Data = []
    print("Enter number of element :")
    Size = int(input())
    
    print("enter the element :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
        
    print("Input data :",Data)
    
    output = list(filterX(CheakEven,Data))
    print("Output after Filter : ",output)
    
    moutput = list(mapX(Increase,output))
    print("Output after map : ",moutput)
    
    result = reduce(Add, moutput)
    print("Output after reduce : ",result)
           
if __name__ == "__main__":
    main()