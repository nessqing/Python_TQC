# 設計說明：
# 請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，第二列之後是個人記錄。請輸出檔案內容並顯示男生人數和女生人數（根據"性別"欄位，0為女性、1為男性）。
#
# 輸入輸出：
# 輸入說明
# 讀取read4.dat
#
# 輸出說明
# 讀取檔案內容，並格式化輸出男生人數和女生人數
#
# 範例輸入
# 無
# 學號 姓名 性別 科系
# 101 陳小華 0 餐旅管理
# 202 李小安 1 廣告
# 303 張小威 1 英文
# 404 羅小美 0 法文
# 505 陳小凱 1 日文
# 範例輸出
# 學號 姓名 性別 科系
#
# 101 陳小華 0 餐旅管理
#
# 202 李小安 1 廣告
#
# 303 張小威 1 英文
#
# 404 羅小美 0 法文
#
# 505 陳小凱 1 日文
# Number of males: 3
# Number of females: 2

m = 0
f = 0

with open("read4.txt","r",encoding="utf-8") as file:
    l1 = file.readlines()
    for i in l1:
        print(i)
        l2 = i.split()
        if l2[2] == "1":
            m += 1
        elif l2[2] == "0":
            f += 1
    print(f"Number of males: {m}")
    print(f"Number of females: {f}")

