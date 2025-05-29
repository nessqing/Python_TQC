# 設計說明：
# 請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。
#
# 輸入輸出：
# 輸入說明
# 十個整數
#
# 輸出說明
# 偶數的個數
# 奇數的個數
#
# 範例輸入
# 69
# 48
# 19
# 91
# 83
# 22
# 18
# 37
# 82
# 40
#
# 範例輸出
# Even numbers: 5
# Odd numbers: 5

even = 0
odd = 0
count_loop = 10
while 1:
    num = eval(input())
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    count_loop -= 1
    if count_loop == 0:
        break
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")