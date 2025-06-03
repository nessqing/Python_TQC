# 設計說明：
# 請撰寫一程式，讓使用者輸入一字串和一字元，並將此字串及字元作為參數傳遞給名為compute()的函式，此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。
#
# 輸入輸出：
# 輸入說明
# 一個字串和一個字元
#
# 輸出說明
# 字串中指定字元出現的次數
#
# 範例輸入
# Our country is beautiful
# u
# 範例輸出
# u occurs 4 time(s)

def compute(u1, u2):
    count_word = 0
    for item in range(len(u1)):
        if u2 == u1[item]:
            count_word += 1
    print(f"{u2} occurs {count_word} time(s)")

compute(input(),input())


        
