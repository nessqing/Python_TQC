### 1XX
- 格式
  - float : {x.2f}
  - 算空格 : 複製答案輸出格式
  - 總共格且往左靠 {:<5}
  - 總共格且往左靠 {:>5}
---
### 2XX : 
> if, elif
- 203 : 閏年
- 205 : isalpha, isdigit
---
### 3XX
- 306 : n! = 1 * 2 * 3 \*...* n
- 307 : 99乘法控制
- 308 : 字串轉成數字相加
- 309 : 注意格式
- 310 : 
  -  1 到 n 不包含 n <- 重點
  - $\frac{1}{1+\sqrt{2}} + \frac{1}{\sqrt{2}+\sqrt{3}} + \frac{1}{\sqrt{3}+\sqrt{4}} + ... + \frac{1}{\sqrt{n-1}+\sqrt{n}}$
---
### 4XX
- 403 : 一行 10 個數字
- 404 : 反著印 [::-1]
- 410 : 等腰三角形
  - 控制行數
  - 控制空白
  - 控制星號
### 5XX
> 💡function 放在最上面
- 502 : 從函式外面給參數
- 506 :
  > 解二元一次的公式為
  > $$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
  
  > $$ b^2 - 4ac > 0, 有 2個解$$
  
  > $$ b^2 - 4ac = 0, 有 1個解$$

  > $$ b^2 - 4ac > 0, 有 無解$$ 
- 507 : 判斷質數
- 508 : 最大公因數, gcd
- 509 : 最大公因數求和, gcd 
- 510 : 費式數列

### 6XX
- 603 : print 裡面的 join 只能加文字
- 604 : 暫時用 import Counter, 然後剩下待說明 ( //todo )
- 605 : 使用到 list 的 max, min, remove
- 606 : 控制行數
- 607 : 開一個包含 3 個 list 的 list
  - [[],[],[]]
- 608 : 找 list 9 個數
  - 會使用到 list.index, 整除//, 取餘數%
- 609 : 開 2 個 2x2 的 list, 一直複製貼上

### 7XX
- 701 : tuple 增加是用 (num,) 
- 702 : tuple 可以直接相加, sorted tuple 會回傳一個 list 型態的回來
- 704 : set() 裡面有 s.add 增加元素
- 705 : set() 是用 add 增加元素, 
  - 判斷用 issubset, issuperset
- 706 : 將句子轉成小寫放進 set, 利用 set 濾掉重複然後 count 數量
- 707 : 記得要 sorted 排序後傳回
  1. union
  2. intersection
  3. difference
  4. symmetric_difference
- 708 : 兩個 dict 相加用 dict1.update(dict2)
  - 用 sorted 排序 key 輸出
- 710 : 搜尋 key, 用 key in dictionary 判斷 true or flase

### 8XX
- 801 : string 可以看成是一個 dict，可以直街 for
- 802 : 轉 ASCII 用 ord
- 803 : 將句子單字用 split 分割放入 list, 取 list 後面三個, 用 join 把它們串再一起
- 804 : 全部轉成大寫用 upper, 只有開頭大寫用 title, title 是第一個 upper 其他保持 lower
- 805 : f"" 裡的{}, align center is ^
- 807 : 切割字串放入 list, 再轉成 int 的 list
- 808 : 直接把字串的符號用 replace 拿掉, 在用 isdigit 判斷
- 809 : 判斷 password.isalnum() 只有包含英文和數字的情況下會返回 true 不能有類似符號的東西
- 810 : 用 split 分割倒入新的 list 

### 9XX : 
> 讀取檔案的指標是從頭指到尾, 如有需要用 seek 
- 901 : 將字串寫入一個檔案, 檔案裡面的顯示要換行 "\n"
- 902 : 將數字split讀取放到陣列, 之後再用 for 迴圈相加
- 903 : write file 的時候選擇 "a" 可保留之前的文字
- 904 : 
  1. 先用 readlines 倒入 list, 再來用 strip 去頭尾的空白和空格 放入一個乾淨的 list
  2. 開三個 list 分別 名字, 身高, 體重
  3. 用 for 切片一個物件, 然後 split 放入一個乾淨的 templist
  4. 分別放入 3 個 list類別
  5. 用 index 去 list 找最大的身高或體重
- 905 : 讀取寫入分開比較方便
- 907 : split 算行數, split 算字數,
- 908 : 
  - split 成 list, 
  - 然後把它轉成 set 塞選唯一值, 
  - 然後用 sorted 排序回傳成一個 list
  - 在用 list.count 去 for 排序過的唯一值看哪一個等於使用者輸入的次數
- 909 : 寫入檔案讀行
- 910 : 
  - 直接先用 readlines 拆行進入 list, 
  - 再來用 split.list 去判斷男生女生