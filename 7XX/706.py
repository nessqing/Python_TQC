# 設計說明：
# 全字母句（Pangram）是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子。請撰寫一程式，要求使用者輸入一正整數k（代表有k筆測試資料），每一筆測試資料為一句子，程式判斷該句子是否為Pangram，並印出對應結果True（若是）或False（若不是）。
#
# 提示：不區分大小寫字母
#
# 輸入輸出：
# 輸入說明
# 先輸入一個正整數表示測試資料筆數，再輸入測試資料
#
# 輸出說明
# 輸入的資料是否為全字母句
#
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示 第1組
# 3
# The quick brown fox jumps over the lazy dog
# True
# Learning Python is funny
# False
# Pack my box with five dozen liquor jugs
# True
#
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示 第2組
# 2
# Quick fox jumps nightly above wizard
# True
# These can be weapons of terror
# False

num = eval(input())

for i in range(num):
    sentence = input()
    countLen= set(sentence.lower().replace(" ", ""))
    if len(countLen) >= 26:
        print(f"True")
    else:
        print(f"False")

