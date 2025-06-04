# 設計說明：
# 請撰寫一程式，要求使用者輸入檔案名稱data.txt和一字串s，顯示該檔案的內容。接著刪除檔案中的字串s，顯示刪除後的檔案內容並存檔。
#
#
# 輸入輸出：
# 輸入說明
# 輸入data1.txt及一個字串
#
# 輸出說明
# 先輸出原檔案內容，再輸入刪除指定字串後的新檔案內容
#
# 範例輸入1
# data.txt
# Tomato
# 範例輸出1
# === Before the deletion
# Apple Kiwi Banana
# Tomato Pear Durian
#
# === After the deletion
# Apple Kiwi Banana
#  Pear Durian

# 範例輸入2
# data1.txt
# Kiwi
# 範例輸出2
# === Before the deletion
# Apple Kiwi Banana
# Tomato Pear Durian
#
# === After the deletion
# Apple Banana
# Tomato Pear Durian

filename = input()
replace_word = input()

print(f"=== Before the deletion")
with open(filename,"r",encoding="utf-8") as file:
    content = file.read()
    print(content)

print(f"=== After the deletion")
with open(filename,"w",encoding="utf-8") as file:
    content1 = content.replace(replace_word,"")
    print(content1)
    file.write(content1)
