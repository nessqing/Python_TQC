# 設計說明：
# 請撰寫一程式，讓使用者輸入一字串，分別將該字串轉換成全部大寫以及每個字的第一個字母大寫。
#
# 輸入輸出：
# 輸入說明
# 一個字串
#
# 輸出說明
# 全部大寫
# 每個字的第一個字母大寫
#
# 範例輸入
# learning python is funny
# 範例輸出
# LEARNING PYTHON IS FUNNY
# Learning Python Is Funny

user_input = input()

print(f"{user_input.upper()}")
print(f"{user_input.title()}")