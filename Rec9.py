i = 1

def Display(No):
    global i
    if(i <= No):
        print(i)
        i+=1
        Display(No)
    
def main():
    
   Display(5)
   
if __name__ == "__main__":
    main()