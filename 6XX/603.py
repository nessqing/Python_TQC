# 設計說明：
# 請撰寫一程式，要求使用者輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字。
#
# 輸入輸出：
# 輸入說明
# 十個數字
#
# 輸出說明
# 由大到小排序，顯示最大的3個數字
#
# 範例輸入1
# 40
# 32
# 12
# 29
# 20
# 19
# 38
# 48
# 57
# 44
# 範例輸出1
# 57 48 44
#
# 範例輸入2
# 139
# 246
# 15
# 38
# 77
# 122
# 42
# 30
# 100
# 1
# 範例輸出2
# 246 139 122

mylist = []
result = []

for i in range(5):
    mylist.append(eval(input()))
temp_mylist = sorted(mylist,reverse=True)

for i in range(3):
    result.append(str(temp_mylist[i]))
print(" ".join(result))
