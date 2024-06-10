

def Sub(A,B):
    return A-B

def Smartsub(FPTR):
    def Inner(A,B):
        if(A<B):
            A,B =B,A
        return FPTR(A,B)
    return Inner

def main():
    SubX = Smartsub(Sub)
    
    Ret = SubX(10,7)
    print("sub is",Ret)
    
    Ret = SubX(7,10)
    print("sub is",Ret)
    
      
if __name__ == "__main__":
    main()