

Add = lambda A,B:  A+B
    

sub = lambda A,B: A-B
     
      
def Marvellous(Value1,Value2):
    Ans1 = Add(Value1,Value2)
    
    Ans2 = sub(Value1,Value2)
  
   return Add,sub

def main():
    Arr = Marvellous(11,7)
    print("Add is :",Arr[0])
    print("sub is :",Arr[1])
   
if __name__ == "__main__":
    main() 