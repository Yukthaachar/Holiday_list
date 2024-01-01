import csv
info1 = []
line1 = []
day1 = []
date1 = []
holiday1 = []
state1 = []
file = open('Holidays_2024.csv', 'r')
info1 = csv.reader(file)
for line in info1:
    date1.append(line[0])
    day1.append(line[1])
    holiday1.append(line[2])
    state1.append(line[3].replace("\n", " ").replace("&", ","))
len1 = len(state1)
for i in range(0, len1, 1):
    list1 = state1[i].split(",")
    if "KA" in state1[i]:
        if "National except " not in state1[i]:
            print(date1[i], day1[i], holiday1[i], "is a holiday for Karnataka")
    if "National".strip() in state1[i].strip():
        if "KA" not in state1[i]:
            print(date1[i], day1[i], holiday1[i], "is a holiday for Karnataka")







