# 設計說明：
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。
#
# 輸入輸出：
# 輸入說明
# 一個正整數
#
# 輸出說明
# 計算n!的值
#
# 範例輸入
# 15
# 範例輸出
# 1307674368000

num = eval(input())
total = 1
for i in range(1,num+1):
    total *= i
print(total)