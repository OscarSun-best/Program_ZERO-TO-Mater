from random import choice
class computer_walk :
    def __init__(self,number_walk=5000):
        self.number_walk =  number_walk

        self.x_value = [0]
        self.y_value = [0]
    def get_step(self):
        while len(self.x_value)  < self.number_walk:
            x_long = choice([0,1,2,3,4])
            y_long = choice({0,1,2,3,4}) 
            x_dirction = choice([1,-1]) * x_long
            y_dirction = choice([-1,-1]) * y_long

            self.x = self.x_value[-1] + y_dirction
            self.y = self.y_value[-1] + x_dirction


            self.x_value.append(self.x)
            self.y_value.append(self.y)




            
    
    