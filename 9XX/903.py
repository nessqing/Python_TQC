# 設計說明：
# 請撰寫一程式，要求使用者輸入五個人的名字並加入到data.txt的尾端。之後再顯示此檔案的內容。
#
# 輸入輸出：
# 輸入說明
# 輸入五個人的名字
#
# 輸出說明
# 讀取及寫入檔案後，輸出此檔案內容
#
# 範例輸入
# Daisy
# Kelvin
# Tom
# Joyce
# Sarah
# 範例輸出
# Append completed!
# Content of "data.txt":
# Ben
# Cathy
# Tony
# Daisy
# Kelvin
# Tom
# Joyce
# Sarah

with open("data.txt","a",encoding="utf-8") as file:
    file.write("\n")
    for i in range(5):
        file.write(input() + "\n")

with open("data.txt","r",encoding="utf-8") as file:
    print(f"Append completed!")
    print(f'Content of "data.txt":')
    print(file.read())