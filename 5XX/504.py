# 設計說明：
# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳的值。
#
# 輸入輸出：
# 輸入說明
# 兩個整數
#
# 輸出說明
# a**b 的值
#
# 範例輸入
# 14
# 3
# 範例輸出
# 2744

def compute(a, b):
    return a**b

a = eval(input())
b = eval(input())

print(compute(a,b))