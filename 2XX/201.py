# 設計說明：
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）。
#
# 輸入輸出：
# 輸入說明
# 一個正整數
#
# 輸出說明
# 判斷是否為偶數
#
# 範例輸入1
# 56
# 範例輸出1
# 56 is an even number.
#
# 範例輸入2
# 21
# 範例輸出2
# 21 is not an even number.
a = eval(input())
if a % 2 == 0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is not an even number.")