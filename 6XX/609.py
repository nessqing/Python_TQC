# 設計說明：
# 請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果。
#
# 輸入輸出：
# 輸入說明
# 兩個2*2矩陣，皆輸入整數
#
# 輸出說明
# 矩陣1的內容
# 矩陣2的內容
# 矩陣1及矩陣2相加的結果
#
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# Enter matrix 1:
# [1, 1]: 3
# [1, 2]: 5
# [2, 1]: 7
# [2, 2]: 5
# Enter matrix 2:
# [1, 1]: 6
# [1, 2]: 9
# [2, 1]: 8
# [2, 2]: 3
# Matrix 1:
# 3 5
# 7 5
# Matrix 2:
# 6 9
# 8 3
# Sum of 2 matrices:
# 9 14
# 15 8

a = [[0,0],[0,0]]
b = [[0,0],[0,0]]

print(f"Enter matrix 1:")
for i in range(2):
    for j in range(2):
        a[i][j] = eval(input(f"[{i+1}, {j+1}]: "))

print(f"Enter matrix 2:")
for i in range(2):
    for j in range(2):
        b[i][j] = eval(input(f"[{i+1}, {j+1}]: "))

print(f"Matrix 1:")
for i in range(2):
    for j in range(2):
        print(f"{a[i][j]}", end=" ")
    print()

print(f"Matrix 2:")
for i in range(2):
    for j in range(2):
        print(f"{b[i][j]}", end=" ")
    print()

print(f"Sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        print(f"{a[i][j] + b[i][j]}", end=" ")
    print()