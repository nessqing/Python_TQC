### 1XX
- 格式
  - float : {x.2f}
  - 算空格 : 複製答案輸出格式
  - 總共格且往左靠 {:<5}
  - 總共格且往左靠 {:>5}
---
### 2XX
- if, elif
   - 閏年
   - isalpha, isdigit
---
### 3XX
- 306 : n! = 1 * 2 * 3 \*...* n
- 307 : 99乘法控制
- 308 : 字串轉成數字相加
- 309 : 注意格式
- 310 : 
  -  1 到 n 不包含 n
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
> - 507 : 判斷質數
> - 508 : 最大公因數, gcd
> - 509 : 最大公因數求和, gcd 
> - 510 : 費式數列

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