# 範例輸入
# I
# enjoy
# learning
# Python
#
# 範例輸出
# |         I      enjoy|
# |  learning     Python|
# |I          enjoy     |
# |learning   Python    |

a = input()
b = input()
c = input()
d = input()

print(f"|{a:>10} {b:>10}|")
print(f"|{c:>10} {d:>10}|")
print(f"|{a:<10} {b:<10}|")
print(f"|{c:<10} {d:<10}|")
