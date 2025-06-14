# 設計說明：
# 請撰寫一程式，自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。
#
# 輸入輸出：
# 輸入說明
# 輸入兩個詞典，直至end結束輸入
#
# 輸出說明
# 合併兩詞典，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值
#
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# Create dict1:
# Key: a
# Value: apple
# Key: b
# Value: banana
# Key: d
# Value: durian
# Key: end
# Create dict2:
# Key: c
# Value: cat
# Key: e
# Value: elephant
# Key: end
# a: apple
# b: banana
# c: cat
# d: durian
# e: elephant

dic_1 = dict()
dic_2 = dict()

print(f"Create dict1:")
while 1:
    key = input("key: ")
    if key == "end":
        break
    dic_1[key] = input("Value: ")

print(f"Create dict2:")
while 1:
    key = input("key: ")
    if key == "end":
        break
    dic_2[key] = input("Value: ")

dic_1.update(dic_2)

for item in sorted(dic_1.keys()):
    print(f"{item}: {dic_1[item]}")