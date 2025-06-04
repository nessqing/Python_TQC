# 設計說明：
# 請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）
#
# 輸入輸出：
# 輸入說明
# 讀取read.txt的內容，以及檔案中某單字出現的次數
#
# 輸出說明
# 輸出符合次數的單字，並依單字的第一個字母大小排序
#
# 範例輸入
# read3.txt
# 3
# 範例輸出
# a
# is
# programming

filename = input()
num = eval(input())

with open(filename,"r",encoding="utf-8") as file:
    r = file.read()
    l = r.split()
    set1 = set(l)
    l2 = sorted(set1)
    for i in l2:
        if l.count(i) == num:
            print(i,end="\n")
