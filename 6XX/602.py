# 設計說明：
# 請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。
#
# 提示：J、Q、K以及A分別代表11、12、13以及1。
#
# 輸入輸出：
# 輸入說明
# 5張牌數
#
# 輸出說明
# 5張牌的數值總和
#
# 範例輸入
# 5
# 10
# K
# 3
# A
# 範例輸出
# 32
total = 0

for i in range(5):
    num = input()
    if num == "A":
        total += 1
    elif num == "J":
        total += 11
    elif num == "Q":
        total += 12
    elif num == "K":
        total += 13
    else:
        total += int(num)
print(total)