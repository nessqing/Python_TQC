# 設計說明：
# 請撰寫一程式，將使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，此函式將回傳x和y的乘積。
#
# 輸入輸出：
# 輸入說明
# 兩個整數
#
# 輸出說明
# 兩個整數相乘之乘積
#
# 範例輸入
# 56
# 11
# 範例輸出
# 616

def compute(x, y):
    return x * y

x = eval(input())
y = eval(input())

print(compute(x,y))
