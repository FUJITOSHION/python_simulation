import math

print('x=1e15の場合')
x = 1e15

res1 = math.sqrt(x+1)-math.sqrt(x)
res2 = 1/(math.sqrt(x+1) + math.sqrt(x))

print("通常の計算方法", res1)
print("分子を有理化した計算方法", res2)
print('-'*20)


print('x=1e16の場合')
x = 1e16

res1 = math.sqrt(x+1)-math.sqrt(x)
res2 = 1/(math.sqrt(x+1) + math.sqrt(x))

print("通常の計算方法", res1)
print("分子を有理化した計算方法", res2)
print('-'*20)
