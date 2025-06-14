# 設計說明：
# 請撰寫一程式，要求使用者輸入檔名data3.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。
#
# 輸入輸出：
# 輸入說明
# 輸入data.txt及兩個字串（分別為s1、s2，字串s1被s2取代）
#
# 輸出說明
# 輸出檔案中的內容
# 輸出取代指定字串後的檔案內容
#
# 範例輸入
# data.txt
# pen
# sneakers
# 範例輸出
# === Before the replacement
# watch shoes skirt
# pen trunks pants
# === After the replacement
# watch shoes skirt
# sneakers trunks pants

filename = input()
s1 = input()
s2 = input()

with open(filename,"r",encoding="utf-8") as file:
    content = file.read()
    print(f"=== Before the replacement")
    print(content)
    content = content.replace(s1,s2)
    print(f"=== After the replacement")
    print(content)