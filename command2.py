import sys
def main():
    print("Demonstration of command line arguments")
    
    print("number of command line arguments are : ",len(sys.argv))
    
    value1 = int(sys.argv[1])
    value2 = int(sys.argv[2])
    Ans = value1 + value2
    print("Additon is : ",Ans)
   
if __name__ == "__main__":
    main()    