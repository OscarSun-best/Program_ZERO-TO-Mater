list_ = []
with open("name.csv", "w") as file:
    while True:
        try:
            name = input("what is you name(or quit to stop)?")
            phone_number =  int(input("what is your phone number!"))
        except ValueError as a:
            print(f"can't be done because of {a}")
            phone_number =  int(input("what is your phone number!"))
        if (name or phone_number) == "quit":
            file.save
            break
        elif (name or phone_number) == "" :
            print("enter again!")
        file.write(f"{name} ,{phone_number}\n")
        ALL_one = {"name" : name  ,"phone_number" : phone_number}
        list_.append(ALL_one)


def print_all():
        print("Content :")
        for All_list in list_ :
            print(f"{All_list[name]} : {All_list[phone_number]}")
def ask_anser():
    ask = input("Enter a name to search for their phone number (or 'quit' to exit):")
    print(f"{ask}'s phone_number : {list_[ask]}")



def get_phone_number(phone_number): ## Get the phone the phone number
    return list_[phone_number]







         
    
    
