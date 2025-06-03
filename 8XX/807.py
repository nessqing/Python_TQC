# 設計說明：
# 請撰寫一程式，要求使用者輸入一字串，該字串為五個數字，以空白隔開。請將此五個數字加總（Total）並計算平均（Average）。
#
# 輸入輸出：
# 輸入說明
# 一個字串（五個數字，以空白隔開）
#
# 輸出說明
# 總合
# 平均 (輸出浮點數到小數點後第一位)
#
# 範例輸入
# -2 34 18 29 -56
# 範例輸出
# Total = 23
# Average = 4.6

user_input = input()
l1 = user_input.split(" ")
l2 = []

for i in l1:
    l2.append(int(i))

print(f"Total = {sum(l2)}")
print(f"Average = {sum(l2)/5:.1f}")