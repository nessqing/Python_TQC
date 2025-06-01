# 設計說明：
# 請撰寫一程式，利用一維串列存放使用者輸入的12個正整數（範圍1~99）。顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果。
#
# 提示：輸出每一個數字欄寬設定為3，每3個一列，靠右對齊。
#
# 輸入輸出：
# 輸入說明
# 12個正整數（範圍1~99）
#
# 輸出說明
# 格式化輸出12個正整數
# 12個數字中，索引為偶數的數字相加總合
#
# 範例輸入
# 56
# 45
# 43
# 22
# 3
# 1
# 39
# 20
# 93
# 18
# 44
# 83
# 範例輸出
#  56 45 43
#  22  3  1
#  39 20 93
#  18 44 83
# 278

mylist = []
total = 0
count = 0

for i in range(12):
    mylist.append(eval(input()))
for j in range(len(mylist)):
    print(f"{mylist[j]:3}",end="")
    if j % 2 == 0:
        total += mylist[j]
    count += 1
    if count == 3:
        count = 0
        print()

print(total)