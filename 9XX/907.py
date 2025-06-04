# 設計說明：
# 請撰寫一程式，要求使用者輸入檔名read1.txt，顯示該檔案的行數、單字數（簡單起見，單字以空白隔開即可，忽略其它標點符號）以及字元數（不含空白）。
#
# 輸入輸出：
# 輸入說明
# 讀取read.txt
#
# 輸出說明
# 行數
# 單字數
# 字元數（不含空白）
#
# 範例輸入
# read1.txt
# 範例輸出
# 6 line(s)
# 102 word(s)
# 614 character(s)

# f_name = input()
# f_line = f_word = f_char = 0
#
# with open(f_name, 'r') as file:
#     for line in file:
#         f_line += 1
#         f_word += len(line.split())
#         f_char += sum([len(c) for c in line.split()])
#
# print('%d line(s)' %f_line)
# print('%d word(s)' %f_word)
# print('%d character(s)' %f_char)

# read1.txt

file = input()
count_line = 0
count_word = 0
count_char = 0

with open(file, "r", encoding="utf-8") as f:
    for line in f:
        count_line += 1
        count_word += len(line.strip().split())
        count_char += len(line.replace("\n","").replace(" ",""))

print(f"{count_line} line(s)")
print(f"{count_word} word(s)")
print(f"{count_char} character(s)")