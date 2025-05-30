# 設計說明：
# 請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。
#
# 提示1：距離 ((x1-x2)**2+(y1-y2)**2)**0.5
# 提示2：兩座標的歐式距離，輸出到小數點後第4位
#
# 輸入輸出：
# 輸入說明
# 四個數字x1、y1、x2、y2
#
# 輸出說明
# 座標1
# 座標2
# 兩座標的歐式距離
#
# 範例輸入
# 2
# 1
# 5.5
# 8
#
# 範例輸出
# ( 2 , 1 )
# ( 5.5 , 8 )
# Distance = 7.8262

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
distance = ((x1-x2)**2+(y1-y2)**2)**0.5
print(f"( {x1} , {y1} )")
print(f"( {x2} , {y2} )")
print(f"Distance = {distance:.4f}")