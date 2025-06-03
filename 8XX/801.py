# 設計說明：
# 請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的索引。
#
# 輸入輸出：
# 輸入說明
# 一個字串
#
# 輸出說明
# 字串每個字元的索引
#
# 範例輸入
# Sandwich
# 範例輸出
# Index of 'S': 0
# Index of 'a': 1
# Index of 'n': 2
# Index of 'd': 3
# Index of 'w': 4
# Index of 'i': 5
# Index of 'c': 6
# Index of 'h': 7

input_char = input()

for item in range(len(input_char)):
    print(f"Index of '{input_char[item]}': {item}")
