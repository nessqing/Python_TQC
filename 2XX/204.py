# 設計說明：
# 請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。
#
# 輸入輸出：
# 輸入說明
# 兩個整數a、b，及一個算術運算子 (+、-、*、/、//、%）
#
# 輸出說明
# 運算結果 (無須做格式化)
#
# 範例輸入
# 30
# 20
# *
# 範例輸出1
# 600
a = eval(input())
b = eval(input())
c = input()
if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
elif c == "//":
    print(a//b)
elif c == "%":
    print(a%b)