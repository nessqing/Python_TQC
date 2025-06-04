# 設計說明：
# 請撰寫一程式，將使用者輸入的五個人的資料寫入data.dat檔，每一個人的資料為姓名和電話號碼，以空白分隔。再將檔案加以讀取並顯示檔案內容。
#
# 輸入輸出：
# 輸入說明
# 五個人的姓名和電話號碼，以空白分隔
#
# 輸出說明
# 讀取及寫入檔案後，再輸出讀入的檔案名稱及內容
#
# 範例輸入
# Karen 123456789
# Bonnie 235689147
# Simon 987612345
# Louis 675489321
# Andy 019238475
# 範例輸出
# The content of "data.dat":
# Karen 123456789
#
# Bonnie 235689147
#
# Simon 987612345
#
# Louis 675489321
#
# Andy 019238475
#


with open("data4.txt","a",encoding="utf-8") as file:
    for i in range(5):
        file.write(input() + "\n")
        file.write("\n")
with open("data4.txt","r",encoding="utf-8") as file:
        r = file.read()

print(f'# The content of "data.dat":')
print(r)