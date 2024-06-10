
def Display(*Values):
    print(type(Values))
    print(len(Values0))
    print(Values)
    
    for i in range(len(Values)):
        print(Values[i])
    
    

def main():
    print("Demonstration of keywords arguments")
    
    Display(10,20,30,40,50,60)
    
if __name__ == " __main__":
    main()