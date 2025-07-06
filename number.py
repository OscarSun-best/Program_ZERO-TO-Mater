def main():
    Value = []
    x = 0
    while True :
        if x == 3 :
            print("If you want the answer then enter (End)")
        
        try:
            Din  = input("What is the number?")
            if Din == "End" :
               print(f"The aveage is {For_number}")
               break
            Damn = float(Din)
            Value.append(Damn)
        except ValueError:
            print("ples enter a number!")   
        count = len(Value)       
        total = sum(Value) / count
        For_number = f"{total:.2f}"
        print(f"You input is :{Value}")
        x += 1
        
main()

        
            
               