# 輸入說明
# 高、寬
#
# 輸出說明
# 高
# 寬
# 周長
# 面積
#
# 範例輸入
# 23.5
# 19
#
# 範例輸出
# Height = 23.50
# Width = 19.00
# Perimeter = 85.00
# Area = 446.50
height = eval(input())
width = eval(input())

print(f"Height = {height:.2f}")
print(f"Width = {width:.2f}")
print(f"Perimeter = {(height+width)*2:.2f}")
print(f"Area = {(height*width):.2f}")