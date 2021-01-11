F = 1.5
G = 9.80655


def retrofire(t, tf):
    if t >= tf:
        return -F * G
    else:
        return 0.0


t = 0.0
h = 0.01

v = float(input('初速度v0を入力してください:'))
x0 = float(input('初期高度x0を入力してください:'))
tf = float(input('逆噴射開始時刻tfを入力してください:'))
x = x0
print('{:.7f} {:.7f} {:.7f}'.format(t, v, x))

while(x > 0) and (x <= x0):
    t += h
    v += (G + retrofire(t, tf)) * h
    x -= v * h
    print
