
def main():
    print("Enter Number of element that you want to store : ")
    Length = int (input())
    
    Arr = list()
    
    print("Enter the element :")
    
    for i in range(Length):
        value = int(input())
        Arr.append(value)
        
    print("element from list are :")
    for i in range(Length):
        print(Arr[i])
        
    
if __name__ == "__main__":
    main()