

def main():
    print("Enter the first number")
    No1 = int(input())
    
    print("Enter the second number")
    No2 = int(input())
    
    Ans = 0
    
    try:
        Ans = No1 / No2
    
    except Exception as zobj:
        print("Exception occured as",zobj)
        
    
    print("Division is :",Ans)
     
if __name__ == "__main__":
    main()