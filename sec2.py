def CheakEven(Value):
     Result = Value % 2
    
    
     if(Result == 0):
        print("Number is even")
     else:
        print("Number is  odd")    
    
    
def main():
    No = 0
    
    print("Enter number : ")
    No = int(input ())
    
    CheakEven(No)
    
if __name__ == "__main__":
    main()
    