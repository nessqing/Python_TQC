# 設計說明：
# 假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）。
#
# 提示：輸出浮點數到小數點後第一位。
#
# 輸入輸出：
# 輸入說明
# x（min）、y（sec）、z（km）數值
#
# 輸出說明
# 速度
#
# 範例輸入
# 10
# 25
# 3
# 範例輸出
# Speed = 10.8

a_min = eval(input())
a_sec = eval(input())
a_km = (eval(input()))/1.6
a_hour = a_min/60 + a_sec/3600
print(f"Speed = {a_km/a_hour}")