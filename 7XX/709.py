# 設計說明：
# 請撰寫一程式，輸入一顏色詞典color_dict（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），再根據key值的字母由小到大排序並輸出。
#
# 輸入輸出：
# 輸入說明
# 輸入一個詞典，直至end結束輸入
#
# 輸出說明
# 根據key值字母由小到大排序輸出
#
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# Key: Green Yellow
# Value: #ADFF2F
# Key: Snow
# Value: #FFFAFA
# Key: Gold
# Value: #FFD700
# Key: Red
# Value: #FF0000
# Key: White
# Value: #FFFFFF
# Key: Green
# Value: #008000
# Key: Black
# Value: #000000
# Key: end
# Black: #000000
# Gold: #FFD700
# Green: #008000
# Green Yellow: #ADFF2F
# Red: #FF0000
# Snow: #FFFAFA
# White: #FFFFFF

dict1 = dict()
while 1:
    key = input("Key: ")
    if key == "end":
        break
    dict1[key] = input("Value: ")

for item in sorted(dict1.keys()):
    print(f"{item}: {dict1[item]}")