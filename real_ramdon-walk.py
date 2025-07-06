import matplotlib.pyplot as draw
from ramdon_walk import computer_walk

rw = computer_walk(50_000)
rw.get_step()
fig ,ax = draw.subplots()
draw.style.use("fivethirtyeight")
ax.scatter(0,0,c="green",edgecolors="none",s=100)
ax.scatter(rw.x_value[-1],rw.y_value[-1],c="red",edgecolors="none",s=100)
ax.scatter(rw.x_value,rw.y_value,c=rw.x_value,cmap=draw.cm.Blues,edgecolors="none",s=1)


draw.show()

