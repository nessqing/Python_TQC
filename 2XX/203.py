# 設計說明：
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，然後判斷它是否為閏年（leap year）或平年。其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。
#
# 輸入輸出：
# 輸入說明
# 一個正整數
#
# 輸出說明
# 判斷是否為閏年或平年
#
# 範例輸入1
# 1992
# 範例輸出1
# 1992 is a leap year.
#
# 範例輸入2
# 2010
# 範例輸出2
# 2010 is not a leap year.

a = eval(input())
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
    print(f"{a} is a leap year.")
else:
    print(f"{a} is not a leap year.")

