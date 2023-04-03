import math

center_x = -118.2853
center_y = 34.0204
R=8.0
r=1.0
a=4.0

fp = open("spiro.kml","w")
fp.write("<kml xmlns=\"http://earth.google.com/kml/2.0\">\n<Document>\n")

fp.write("<Placemark>\n<Point>\n<coordinates>-118.2853,34.0204</coordinates>\n</Point>\n</Placemark>\n")

t = 0
while t < 16*math.pi:
    fp.write("<Placemark>\n<Point>\n<coordinates>")
    x = ((R+r)*math.cos((r/R)*t) - a*math.cos((1+r/R)*t)) * 0.0004 + center_x
    y = ((R+r)*math.sin((r/R)*t) - a*math.sin((1+r/R)*t)) * 0.0004 + center_y
    fp.write(str(x) + "," + str(y) + "</coordinates>\n</Point>\n</Placemark>\n")
    t += 0.02

fp.write("</Document>\n</kml>")
fp.close()

# import matplotlib.pyplot as plt
# import sys
# import math

# R=4
# r=0.5
# a=1

# t = 0.0
# while t < 16*math.pi:
#     x = ((R+r) * math.cos(t) - (r+a) * math.cos(((R+r)*t)/r))
#     y = ((R+r) * math.sin(t) - (r+a) * math.sin(((R+r)*t)/r))
#     plt.scatter(x, y, s=10)
#     t += 0.08

# plt.show()