# 設計說明：
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，判斷此點是否與點(5, 6)的距離小於或等於15，如距離小於或等於15顯示【Inside】，反之顯示【Outside】。
#
# 提示：計算平面上兩點距離的公式：((x1-x2)**2+(y1-y2)**2)**0.5
#
# 輸入輸出：
# 輸入說明
# 兩個數值x、y
#
# 輸出說明
# 小於或等於15輸出Inside；大於15輸出Outside
#
# 範例輸入1
# 7
# 20
# 範例輸出1
# Inside
#
# 範例輸入2
# 30
# 35
# 範例輸出2
# Outside

x1 = 5
y1 = 6
x2 = eval(input())
y2 = eval(input())
distance = ((x1-x2)**2+(y1-y2)**2)**0.5
if distance <= 15 :
    print("Inside")
else:
    print("Outside")

