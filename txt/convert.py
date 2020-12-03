import re

f = open("txt\\test_2_0.txt", "w+")
v = []
count = 0
for x in f:
    if (count!=0):
        a = x[:-1]
        v.append([ re.sub("[ ]", ",", a) ])
    count +=1
