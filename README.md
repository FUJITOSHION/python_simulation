# 学びを記述
## 第一章pythonにおける数値計算
### 2分法(busection method)
busection methodでは解の存在範囲の上限と下限を調べる。
```math
  f(x)=x^2-2
```
f(p)>0となるp、f(n)<0となるnを求めて、
(p+n)/2を求めて、f((p+n)/2)>0の場合pを上限とする。

### 数値計算における誤差
- 桁落ち
```math
sqrt(x+1) - sart(x)
```
- 丸め誤差
10進数の0.1は、2進数に変換する際に丸により、0.1よりわずかに大き値になるため。

## 第2章
- 1次元運動シミュレーション