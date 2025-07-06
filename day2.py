login_attemps = 0
class User :
    def __init__(self,frist_name,last_name,identity):
        self.frist_name = frist_name
        self.last_name = last_name
        self.identity = identity
        self.login_attempts = 0
    def increment_login_attempts(self):
        self.login_attempts += 1
    def describe_user(self):
        print(f"{self.frist_name} {self.last_name} love to eat {input("what do you like to eat?")}")
        print(f"And his personal identity is {self.identity}")
        self.increment_login_attempts()
    def Turn_xreo(self):
        print(login_attemps - login_attemps)
    def greet_user(self):
        print(f"{self.frist_name} {self.last_name} how are you?")
        self.increment_login_attempts()
        anser = input(":")  
        if anser == "Good":
            print("i am gpod to!")
        elif anser == "No":
            print("I am sorry about that!")
        else:
            exit



my_user = User("Sun","Oscar","shouting")
my_user.describe_user()
my_user.greet_user()
print(my_user.login_attempts)
my_user.Turn_xreo()




    
        