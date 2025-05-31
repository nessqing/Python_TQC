# 設計說明：
# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳從a連加到b的和。
#
# 輸入輸出：
# 輸入說明
# 兩個整數
#
# 輸出說明
# 從a連加到b的和
#
# 範例輸入
# 33
# 66
# 範例輸出
# 1683

def compute(a, b):
    total = 0
    for i in range(a,b+1):
        total += i
    return total

a = eval(input())
b = eval(input())

print(compute(a,b))
