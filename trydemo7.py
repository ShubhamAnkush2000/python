

def main():
    try:
        
         print("Enter the first number")
         No1 = int(input())
    
         print("Enter the second number")
         No2 = int(input())
    
         Ans = 0
    
    
         Ans = No1 / No2
    
    except ZeroDivisionError as zobj:
        print("Divide by zero is not allowed",zobj)
        return
    
    except ValueError as Vobj:
        print("Invalid input :",Vobj)
        return
     
    except Exception as zobj:
        print("Exception occured as",zobj)
        return
    
    finally :
        print("Thank you for using the application")
    
    print("Division is :",Ans)
     
if __name__ == "__main__":
    main()