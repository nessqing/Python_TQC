# 設計說明：
# 請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。
#
# 輸入輸出：
# 輸入說明
# 九個整數
#
# 輸出說明
# 矩陣最大值及其索引
# 矩陣最小值及其索引
#
# 範例輸入
# 6
# 4
# 8
# 39
# 12
# 3
# -3
# 49
# 33
# 範例輸出
# Index of the largest number 49 is: (2, 1)
# Index of the smallest number -3 is: (2, 0)


a = []
for i in range(9):
    a.append(eval(input()))

print(f"Index of the largest number {max(a)} is: ({a.index(max(a)) // 3}, {a.index(max(a)) % 3})")
print(f"Index of the smallest number {min(a)} is: ({a.index(min(a)) // 3}, {a.index(min(a)) % 3})")