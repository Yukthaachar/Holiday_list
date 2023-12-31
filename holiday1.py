f1 = open("Holidays_2024(1).csv", "r")
date1 = []
day1 = []
holiday1 = []
state1 = []
list2 = []
info1 = f1.readlines()
#print(info1)
len1 = len(info1)
# print(len1)
for i in range(0, len1, 1):
    info2 = info1[i]
    list1 = info2.split(",")
    date1.append(list1[0])
    day1.append(list1[1])
    holiday1.append(list1[2])
    info3 = info2.replace(date1[i], "").replace(day1[i], "").replace(holiday1[i], "").replace(",,,", "").replace("\n",
                                                                                                                 "")
    state1.append(info3)

# print(date1)
# print(day1)
# print(holiday1)
# print(state1)

for i in range(0, len1, 1):
    if "KA" in state1[i]:
        list2.append(i)
# print(list2)

for i in list2:
    print(date1[i], day1[i], holiday1[i], "is a holiday for Karnataka")
