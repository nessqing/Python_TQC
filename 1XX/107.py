# 輸入輸出：
# 輸入說明
# 五個數字
#
# 輸出說明
# 輸出五個數字
# 總和
# 平均數
#
# 範例輸入1
# 20
# 40
# 60
# 80
# 100
# 範例輸出1
# 20 40 60 80 100
# Sum = 300.0
# Average = 60.0
#
# 範例輸入2
# 88.7
# 12
# 56
# 132.55
# 3
# 範例輸出2
# 88.7 12 56 132.55 3
# Sum = 292.2
# Average = 58.5

a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
e = eval(input())
sum_num = a+b+c+d+e
print(f"{a} {b} {c} {d} {e}")
print(f"Sum = {sum_num:.1f}")
print(f"Average = {sum_num/5:.1f}")