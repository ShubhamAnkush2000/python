import Marvaellousfmr

CheakEven = lambda No: (No % 2 == 0)
Increase = lambda No : No+2   
Add =lambda A,B:A+B
           
def main():
    Data = []
    print("Enter number of element :")
    Size = int(input())
    
    print("enter the element :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
        
    print("Input data :",Data)
    
    output = list(Marvaellousfmr.filterX(CheakEven,Data))
    print("Output after Filter : ",output)
    
    moutput = list(Marvaellousfmr.mapX(Increase,output))
    print("Output after map : ",moutput)
    
    result = Marvaellousfmr.reduceX(Add, moutput)
    print("Output after reduce : ",result)
           
if __name__ == "__main__":
    main()