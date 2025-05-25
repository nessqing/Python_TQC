# 設計說明：
# 請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。
#
# 提示1：建議使用import math模組的math.pow及math.tan
# 提示2：正n邊形面積的公式如下：Area = n*math.pow(s, 2) / (4*math.tan(math.pi/n))
# 提示3：輸出浮點數到小數點後第四位
#
# 輸入輸出：
# 輸入說明
# 正數n、s
#
# 輸出說明
# 正n邊形面積
#
# 範例輸入
# 8
# 6
# 範例輸出
# Area = 173.8234
import math
n = eval(input())
s = eval(input())
# math.pow()
area = n*math.pow(s, 2) / (4*math.tan(math.pi/n))
print(f"Area = {area:.4f}")