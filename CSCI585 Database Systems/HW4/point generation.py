import math
from os import write

center_x = -118.2853
center_y = 34.0204
R=8.0
r=1.0
a=4.0

fp = open("spiro.json","w")
fp.write("[\n")

t = 0
count = 0
while t < 16*math.pi:
    print(count)
    fp.write("  {\n    \"loc\": [")
    x = ((R+r)*math.cos((r/R)*t) - a*math.cos((1+r/R)*t)) * 0.0004 + center_x
    y = ((R+r)*math.sin((r/R)*t) - a*math.sin((1+r/R)*t)) * 0.0004 + center_y
    fp.write(str(x) + "," + str(y) + "]\n  }")
    if count != 502:
        fp.write(",")
    fp.write("\n")
    t += 0.1
    count+=1
fp.write("]\n")
fp.close()