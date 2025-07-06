import csv
import matplotlib.pyplot as draw
from datetime import datetime as time
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader_ = csv.reader(f)
    highest = next(reader_)
    highest_temp_list, lower_temp_list, date_time = [] ,[] ,[]
    x = 0
    for row in reader_ : 
        try:
            lower_temp_list.append(int(row[6]))

            date_time.append(time.strptime(row[2], "%Y-%m-%d"))
        
            highest_temp_list.append(int(row[5]))

        except ValueError: 
            print(f"their is a error at {row}") 

# The code reads a CSV file named 'sitka_weather_2018_simple', 
# extracts the values from the 6th column (index 5) (means the lowest temperature),
# 4th column is the hightest temperture , and 2nd is the date of the temperture
# at last append all the things in the the list
draw.style.use('seaborn-v0_8')
fig, ax = draw.subplots()
ax.plot(date_time, lower_temp_list, linewidth = 2, c= "red",alpha = 0.5)
ax.plot(date_time, highest_temp_list ,linewidth = 2,c="blue" , alpha = 0.5)


ax.fill_between(date_time,lower_temp_list, highest_temp_list ,alpha=0.1 ,facecolor= "blue")
ax.set_title("sitka's weather in 2018", fontsize = 24)
ax.set_ylabel("Temperater(F)", fontsize = 16)
ax.set_xlabel("",fontsize = "16")

ax.tick_params(axis="both",which = 'major',labelsize = 16)

# So here is drawing a line chart with two lines (blue line is the hightest temperature),(red line is the lowest temperature),
# And the line style we use is seaborn which means Line chat ,
# in line 36 ax.tick_parms is the frontsize of the words on x and yasix . 
# At last we show the line in line 42.
draw.show()