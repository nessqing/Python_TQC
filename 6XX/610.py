# 設計說明：
# 請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。
#
# 提示1：平均溫度輸出到小數點後第二位。
# 提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。
#
# 輸入輸出：
# 輸入說明
# 四週各三天的溫度
#
# 輸出說明
# 平均溫度
# 最高溫度
# 最低溫度
#
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# 下圖中的 粉紅色點(_) 為 空格
# Week_1:
# Day_1:23.1
# Day_2:24
# Day_3:23.5
# Week_2:
# Day_1:32
# Day_2:33
# Day_3:35.3
# Week_3:
# Day_1:29
# Day_2:30
# Day_3:26
# Week_4:
# Day_1:27.6
# Day_2:25
# Day_3:28.8
# Average:_28.11
# Highest:_35.3
# Lowest:_23.1

mylist = []
for i in range(1,5):
    print(f"Week {i}:")
    for j in range(3):
        mylist.append(eval(input(f"Day {j+1}:")))
print(f"Average: {sum(mylist)/len(mylist):.2f}")
print(f"Highest: {max(mylist)}")
print(f"Highest: {min(mylist)}")
