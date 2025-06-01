# 設計說明：
# 請撰寫一程式，讓使用者輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數。
#
# 提示：假設樣本中只有一個眾數。
#
# 輸入輸出：
# 輸入說明
# 十個整數
#
# 輸出說明
# 眾數
# 眾數出現的次數
#
# 範例輸入
# 34
# 18
# 22
# 32
# 18
# 29
# 30
# 38
# 42
# 18
# 範例輸出
# 18
# 3

from collections import Counter

nums = []

for i in range(10):
    nums.append(eval(input()))
counter = Counter(nums).most_common(1)

print(f"{counter[0][0]}")
print(f"{counter[0][1]}")


