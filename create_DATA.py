import matplotlib.pyplot as draw

down_line = range(1,5001)
y_raa = [x**3 for x in down_line]
draw.style.use('seaborn-v0_8-dark-palette')
fig,ax = draw.subplots()
ax.scatter(down_line,y_raa,c=y_raa,cmap=draw.cm.Blues,s = 20)

ax.set_title("ramdon_number",fontsize=24)
ax.set_xlabel("ramdon....",fontsize = 14)
ax.set_ylabel("NUMBER",fontsize = 14)

ax.tick_params(axis="both",which="major",labelsize = 14)
ax.axis([0, 6100, 0, 12225])
draw.show()