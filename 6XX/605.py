# 設計說明：
# 請撰寫一程式，讓使用者輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。
#
# 提示：平均值輸出到小數點後第二位。
#
# 輸入輸出：
# 輸入說明
# 十個數字
#
# 輸出說明
# 總和
# 平均
#
# 範例輸入
# 89
# 78
# 67
# 80
# 75
# 98
# 77
# 89
# 76
# 60
# 範例輸出
# 631
# 78.88

mylist = []

for i in range(10):
    mylist.append(eval(input()))

mylist.remove(max(mylist))
mylist.remove(min(mylist))

print(f"{sum(mylist)}")
print(f"{sum(mylist) / len(mylist):.2f}")