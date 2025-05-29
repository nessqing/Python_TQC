# 設計說明：
# 某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。請撰寫一程式，輸入五張選票，輸入值如為1即表示針對1號候選人投票；輸入值如為2即表示針對2號候選人投票，如輸入其他值則視為廢票。每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；如最終計算有相同的最高票數者或無法選出最高票者，顯示【=> No one won the election.】。
#
# 輸入輸出：
# 輸入說明
# 五個正整數（1、2或其他）
#
# 輸出說明
# 每次投完後需印出目前每位候選人的得票數
# 五張選票投票完成，最後印出最高票者為當選人
#
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# 2
# Total votes of No.1: Nami =  0
# Total votes of No.2: Chopper =  1
# Total null votes =  0
# 1
# Total votes of No.1: Nami =  1
# Total votes of No.2: Chopper =  1
# Total null votes =  0
# 8
# Total votes of No.1: Nami =  1
# Total votes of No.2: Chopper =  1
# Total null votes =  1
# 2
# Total votes of No.1: Nami =  1
# Total votes of No.2: Chopper =  2
# Total null votes =  1
# 2
# Total votes of No.1: Nami =  1
# Total votes of No.2: Chopper =  3
# Total null votes =  1
# => No.2 Chopper won the election.

nami = 0
chopper = 0
votes = 0
for i in range(5):
    num = eval(input())
    if num == 1:
        nami += 1
    elif num == 2:
        chopper += 1
    else:
        votes += 1
    print(f"Total votes of No.1: Nami =  {nami}")
    print(f"Total votes of No.2: Chopper =  {chopper}")
    print(f"Total null votes =  {votes}")
if nami > chopper:
    print(f"=> No.1 Chopper won the election.")
elif nami < chopper:
    print(f"=> No.2 Chopper won the election.")
else:
    print(f"No one won the election.")


