# 範例輸入
# 85
# 4
# 299
# 478
#
# 範例輸出
# |   85     4|
# |  299   478|
# |85    4    |
# |299   478  |


a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())

print(f"|{a:>5} {b:>5}|")
print(f"|{c:>5} {c:>5}|")
print(f"|{a:<5} {b:<5}|")
print(f"|{c:<5} {c:<5}|")
