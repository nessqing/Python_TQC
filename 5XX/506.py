# 設計說明：
# 請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式 a * x**2 + b * x + c = 0 的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has no root.】
#
# 提示：
# 輸出有順序性
# 回傳方程式的解，無須考慮小數點位數
#
# 3. 輸入輸出：
# 輸入說明
# 三個整數，分別為a、b、c
#
# 輸出說明
# 代入一元二次方程式，回傳方程式解；如無解則輸出【Your equation has no root.】
#
# 範例輸入1
# 2
# -3
# 1
# 範例輸出1
# 1.0, 0.5
#
# 範例輸入2
# 9
# 9
# 8
# 範例輸出2
# Your equation has no root.
#
# 範例輸入3
# 1
# 2
# 1
# 範例輸出3
# -1.0

def compute(a,b,c):
    temp = b**2 - 4*a*c
    if temp < 0:
        print(f"Your equation has no root.")
    elif temp == 0 :
        print(f"{(-b + (b**2 - 4*a*c)) / (2*a)}")
    else:
        print(f"{(-b + (b**2 - 4*a*c)) / (2*a)}, {(-b - (b**2 - 4*a*c)) / (2*a)}")

a = eval(input())
b = eval(input())
c = eval(input())

compute(a,b,c)