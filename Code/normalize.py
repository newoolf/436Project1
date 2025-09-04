filepath = "../Project1_Data_F25/Project1_Data/groupA.txt"

lines = list()
with open(filepath, 'r') as f:
    for x in f:
        lines.append(x)

coloumnOne = list()
coloumnTwo = list()
coloumnThree = list()
for line in lines:
    parts = line.split(',')
    coloumnOne.append(float(parts[0]))
    coloumnTwo.append(float(parts[1]))
    coloumnThree.append(float(parts[2]))