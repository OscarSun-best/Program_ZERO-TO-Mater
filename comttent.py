studens = []

with open("name.csv") as file :
    for line in file :
        name, house = line.rstrip().split(",")
        student ={"name" : name , "house" : house}
        studens.append(student)
for standant in studens :
    print(f"{standant['name']} is in {standant['house']}")
print(studens)