import numpy as np
import matplotlib.pyplot as plt


G = 9.80665

t = 0.0
h = 0.01

v = float(input('初速度v0を入力してください:'))
x = float(input('初期速度x0を入力してください:'))

print("{:.7f}{:.7f}{:.7f}".format(t, x, v))

tlist = [t]
xlist = [x]

while x >= 0:
    t += h
    v += G * h
    x -= v * h
    print("{:.7f} : {:.7f} : {:.7f}".format(t, x, v))
    tlist.append(t)
    xlist.append(x)

plt.plot(tlist, xlist)
plt.show()
