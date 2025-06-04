# 設計說明：
# 請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。
#
# 提示：輸出浮點數到小數點後第二位。
#
# 輸入輸出：
# 輸入說明
# 讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）
#
# 輸出說明
# 輸出檔案中的內容
# 平均身高
# 平均體重
# 最高者
# 最重者
#
# 範例輸入
# 無
#
# 範例輸出
# Ben 175 65
#
# Cathy 155 55
#
# Tony 172 75
# Average height: 167.33
# Average weight: 65.00
# The tallest is Ben with 175.00cm
# The heaviest is Tony with 75.00kg

with open("read1.txt","r",encoding="utf-8") as file:
    r = file.readlines()

clean_r = []
for i in r:
    temp = i.strip()
    if temp:
        clean_r.append(temp)

names = []
heights = []
weights = []

for item in clean_r:
    temp = item.split()
    name = temp[0]
    height = eval(temp[1])
    weight = eval(temp[2])

    names.append(name)
    heights.append(height)
    weights.append(weight)

print(f"Average height: {sum(heights)/3:.2f}")
print(f"Average weight: {sum(weights)/3:.2f}")
print(f"The tallest is {names[heights.index(max(heights))]} with {max(heights):.2f}cm")
print(f"The heaviest is {names[weights.index(max(weights))]} with {max(weights):.2f}kg")
