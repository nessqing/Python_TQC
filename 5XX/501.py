# 設計說明：
# 請撰寫一程式，呼叫函式compute()，該函式功能為讓使用者輸入系別（Department）、學號（Student ID）和姓名（Name）並顯示這些訊息。
#
# 輸入輸出：
# 輸入說明
# 三個字串
#
# 輸出說明
# 系別（Department）
# 學號（Student ID）
# 姓名（Name）
#
# 範例輸入
# Information Management
# 123456789
# Tina Chen
# 範例輸出
# Department: Information Management
# Student ID: 123456789
# Name: Tina Chen

def compute():
    dep = input()
    stu = input()
    name = input()
    print(f"Department: {dep}")
    print(f"Student ID: {stu}")
    print(f"Name: {name}")
compute()