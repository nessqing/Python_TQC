# 設計說明：
# 請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。
#
# 輸入輸出：
# 輸入說明
# 一個正整數
#
# 輸出說明
# 以 * 畫出等腰三角形
# （每列最後一個 * 的右方無空白）
#
# 範例輸入
# 7
# 範例輸出
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
# *************

star = 1
num = eval(input())
for i in range(1, num+1):
    for j in range(num - i):
        print(" ", end="")
    for k in range(star):
        print("*",end="")
    star += 2
    print()