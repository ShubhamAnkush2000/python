

def sub(A,B):
    if(A<B):
        A,B = B,A
    return A-B

def main():
    
    Ret = sub(10,7)
    print("sub is",Ret)
    
    
    Ret = sub(7,10)
    print("sub is",Ret)
    
    
    
if __name__ == "__main__":
    main()