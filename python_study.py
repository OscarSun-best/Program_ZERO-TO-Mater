from plotly.graph_objs import Bar, Layout
from plotly import offline
from random import randint
class Die:
    def __init__(self,surface_die = 6):
        self.surface_die = surface_die
    def roll_die(self):
        return randint(1,self.surface_die)

die = Die()
die1 = Die()

all_results = [die.roll_die() * die1.roll_die() for _  in range(50000)]

all_surface = die.surface_die * die1.surface_die

god_damn = [all_ * all_ for all_ in range(1 , all_surface +1)]

fruquency = [all_results.count(cut) for cut in range(1, all_surface + 1)]

print(fruquency)

x_value = list(range(1 , all_surface + 1))
data = [Bar(x = x_value,y= fruquency)]

x_axis_config = {"title" : "output", "tickvals" : god_damn}
y_axis_config = {"title" : "Die's frequencies"}
my_layout = Layout(title= "roll a die for 50000 times_output",title_x = 0.5,xaxis=x_axis_config , yaxis = y_axis_config)
offline.plot({'data': data ,'layout': my_layout},filename = 'd6.html')

print(die.surface_die)
print(die1.surface_die)
print(all_surface)



    
    


                 