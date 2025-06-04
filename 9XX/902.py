# 設計說明：
# 請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。檔案讀取完成後要關閉。
#
# 輸入輸出：
# 輸入說明
# 讀取read.txt的內容（內容為數字，以空白分隔）
#
# 輸出說明
# 總和
#
# 範例輸入
# 無
#
# 範例輸出
# 660

result = 0

with open("read.txt","r",encoding="utf-8") as file:
     temp_list = file.read().split(" ")
     for i in range(len(temp_list)):
         result += int(temp_list[i])
         
print(result)