# 設計說明：
# 請撰寫一程式，讓使用者輸入兩個正整數a、b（a<=b），輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）以及倍數之個數、總和。
#
# 輸入輸出：
# 輸入說明
# 兩個正整數a、b（a<=b）
#
# 輸出說明
# 格式化輸出兩個正整數之間4或9之倍數（包含a和b）
# 倍數個數
# 倍數總合
#
# 範例輸入1
# 5
# 55
# 範例輸出1
# 8   9   12  16  18  20  24  27  28  32
# 36  40  44  45  48  52  54
# 17
# 513
#
# 範例輸入2
# 4
# 9
# 範例輸出2
# 4   8   9
# 3
# 21

a = eval(input())
b = eval(input())
word_control = 0
num = 0
total = 0

for i in range(a, b+1):
    if i % 4 == 0 or i % 9 == 0:
        print(f"{i:<4}",end="")
        num += 1
        total += i
        word_control += 1
        if word_control % 10 ==0:
            print()
print()
print(num)
print(total)