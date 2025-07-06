def main():
    ding = {"integer" : 0 ,"nagetive" : 0 , "Zero" : 0}
    count = 0
    while True :
        Fuck = input("Enter 5 number!")
        if Fuck.strip() == "":
            print("ples enter a number")
        elif Fuck.strip() == "end":
            for key in ding:
                print(f"{key}: {ding[key]}")
            break
        numbers = Fuck.split()
        for num in numbers :
            try :
                number = int(num)
                if number > 0:
                    ding["integer"] += 1
                elif number < 0:
                    ding["nagetive"] += 1
                elif number == 0:
                    ding["Zero"] += 1
                count += 1
                if count == 6:
                    print("if you wan to end this , ples enter {end} ")  
            except ValueError :
                print(f"print {number} is not an integer!")

main()


        
        
