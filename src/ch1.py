# グローバル変数
a = 2
LIMIT = 1e-20


def f(x):
    return x ** 2 - a


xp = float(input('xpを入力をしてください'))
xn = float(input('xpを入力をしてください'))

while (xp - xn) * (xp - xn) > LIMIT:
    xmid = (xp + xn)/2
    if f(xmid) > 0:
        xp = xmid
    else:
        xn = xmid
    print("{:.15f} {:.15f}".format(xn, xp))
