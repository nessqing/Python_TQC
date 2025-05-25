# 設計說明：
# 請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）。
#
# 提示1：建議使用import math模組的math.pow及math.tan
# 提示2：正五邊形面積的公式：Area = (5*s**2) /(4*math.tan(math.pi/5))
# 提示3：輸出浮點數到小數點後第四位。
#
# 輸入輸出：
# 輸入說明
# 正數s
#
# 輸出說明
# 正五邊形面積
#
# 範例輸入
# 5
# 範例輸出
# Area = 43.0119
import math
s = eval(input())
area = (5*s**2) / (4*math.tan(math.pi/5))
print(f"Area = {area:.4f}")