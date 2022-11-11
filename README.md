
# Python & Discord Bot

環境安裝：
下載python最新版本
https://www.python.org/downloads/windows/

![](https://i.imgur.com/LCYJfAj.png)

記得點選將python加到環境變數中以方便在命令提示字元呼叫python

![](https://i.imgur.com/riWm4hD.png)

測試是否安裝成功

按下win+s並輸入cmd

![](https://i.imgur.com/4qyjNf2.png)

點選看起來黑黑的應用程式

> 可以到Microsoft商店下載Windows Termial Preview  
> ![](https://i.imgur.com/lDUDMs8.png)  
> 可以開啟多個指令視窗  
> 也可以更換指令視窗的背景  


在指令列中輸入
```cmd
python --version
```
與
```cmd
pip --version
```

理論上會出現這樣的結果

![](https://i.imgur.com/QT9Dm2R.png)

> 有問題直接問我ouo


下載Visual Studio Code
https://visualstudio.microsoft.com/zh-hant/downloads/

![](https://i.imgur.com/iPtawm7.png)



在桌面上新增一資料夾
名稱隨意取
![](https://i.imgur.com/NCLGYGv.png)

開啟Visual Studio Code，點選Open Folder
找到你的資料夾並開啟

![](https://i.imgur.com/9Ve9fKT.png)

畫面左方應該會出現這個

![](https://i.imgur.com/zZyAaUQ.png)

接下來就能開始寫程式了...才怪

## Terminal 終端機
剛剛提過Windows Terminal Preview
這裡面的Termianl即為終端機

終端機就是指：使用指令敘述而不是用ui來控制電腦的視窗
通常所有應用程式與瀏覽器，有明確按鈕或介面的這種東西都叫做ui
ui就是一種視覺化的操作，能夠使大眾比較容易上手

Terminal種類：cmd，windows powershell
在跑python程式時也可以直接利用終端機輸入
首先確認你的執行位置在你的資料夾中
如果沒有先使用`cd <檔案位址>`
再打上`python <檔名>`
![](https://i.imgur.com/E5Hyhi4.png)

cmd指令表
https://www.thomas-krenn.com/en/wiki/Cmd_commands_under_Windows


## Python語法與應用

### 基礎語法：

變數(Variable)：
Vary：變化v. 去y + i + able = 可變動的adj.

變數即為某部分記憶體儲存的資料
 
變數取名法：  
通常用有意義的字  
比如：  
`numbers`、`words`  
如果需要多個英文字  
`input_choices`、`inputNumbers`  
注意不可以與`python`內建的關鍵字衝突  
常見關鍵字：  
`if`、`elif`、`else`、`for`、`while`、`try`、`except`  
`break`、`continue`、`in`、`True`、`False`、`def`、`None`  
`global`、`return`  



型態(type)淺說：
「型態」為資料在電腦中儲存的一個標籤，這個標籤決定了資料間能否互相運算或是使用特定功能。

比如：`int`即表示整數型態，他能夠和各種數字型態相加減，但是所得的結果的型態可能會改變

> `int(+-*)int=int`  
> ***`int(/)int=float`***  
> `int(+-*/)float=float` `(float可以先理解成小數)`  
> `float(+-*/)int=float`  
> 判斷技巧：跟`float`扯上關係就回不去`int`了  

第二行的結果說明：  
![](https://i.imgur.com/8MEatRb.png)  
雖然`1/1`顯然可以寫成`1`，但表示為比例的那一刻就成為了有理數。  

![](https://i.imgur.com/QAPmeSW.png)

> `type(變數)`將回傳變數的型態

事實上，各種基本型態是python內建函式庫中的模組(Module)   
每個Module都有自己的標籤  

基本型態表：
| Type | int                    | float                        | str(string)     | bool |
| :----: | :----------------------: | :----------------------------: | :----------: | :---: |
| 說明 | 與數學$\mathbb{Z}$相同 | 任意實數皆會被近似成有限小數 | 字串 |True or False|

> 在`python`中，轉換型態的方法為    
> `變數型態()`    
> 比如：`print(float(2))`、`print(int(3.5))`    
> ![](https://i.imgur.com/eXcFIr0.png)  
> 變數型態的不同將會使輸出結果不同    
> 無法轉換時會報錯    

> 若要換行輸出可在字串內加入`\n`  
> 例如`'你為什麼不問問神奇海螺呢?\n這裡還有沒有第五個章魚哥'`  
> ![](https://i.imgur.com/4tTklCN.png)  

### 運算子operators  
數學運算子Mathematical operators

| 語法       | +          | -          | *        | /        | %        |
| :----------: | :----------: | :----------: |:--------: | :--------: | :--------: |
| 名稱       | 加         | 減         | 乘       | 除       | 取餘數   |
| 運算方向   | 由左至右   | 由左至右   | 由左至右 | 由左至右 | 由左至右 |
| 回傳 | 物件相加 |物件相減 |物件相乘|物件相除|左除以右的餘數(限定數字運算)|
| 運算優先度 | 在乘除之後 | 在乘除之後 | 最優先   | 最優先   | 最優先   |

邏輯運算子[^first]Logical operators

| 語法       | `&&`、`and` | \|\|、`or` | `!`、`not`[^second] | ==         |
| :----------: | :-----------: | :----------: | :----------: | :----------: |
| 名稱       | 且          | 或         | 不         | 等於       |
| 運算方向   | 由左至右    | 由左至右   | 由左至右   | 由左至右   |
| 運算優先度 | 在加減之後  | 再加減之後 | 在加減之後 | 在加減之後 |

[^first]: 邏輯運算子回傳的值皆為布林值
[^second]: `!=`即為`==`的否定敘述

> 布林值可表示為`0或1`，其中`True`表示`1`，`False`表示`0`

邏輯運算子的真值表：
`&&`：
| A   | B   | output |
| :---: | :---: | :------: |
| 0   | 0   | 0      |
| 1   | 0   | 0      |
| 0   | 1   | 0      |
| 1   | 1   | 1      |

> 電路接法：串聯

`||`：
| A   | B   | output |
| :---: | :---: | :------: |
| 0   | 0   | 0      |
| 1   | 0   | 1      |
| 0   | 1   | 1      |
| 1   | 1   | 1      |

> 電路接法：並聯

`!`：
| A   | output |
| :---: | :------: |
| 0   | 1      |
| 1   | 0      |


> 若需要強迫電腦優先運算某些敘述，可以用小括號包含  
> 中括號與大括號另有其涵義  

> 各物件都有自己本身支持的運算子，在使用之前應該先看過API文件  

賦值運算子[^third]
\=
[^third]:`a=a+1`可寫為`a+=1`，`a=a-1`可寫為`a-=1`，乘除同理


名稱：賦值  
運算方向：由右至左   
比如：  
```python
a=2
#a is now 2
a=a+2
#a先取原本的值加上2後再把結果傳給a儲存
```  
運算優先度：最後  
 

### 陣列`list`
什麼是陣列？  
舉例：  
```python
list1 = ['水果','香蕉']
list2 = [0, 3, 5]
```
陣列就是一串資料，每個資料都有一個自己的索引值(`index`)  
陣列中每個元素都是一個變數，意思是可以儲存各種不同型態的物件  
比如：  
```python
from typing import List, Union 
#此模組是為了方便說明陣列中儲存的資料型態
#非必要
#也可以讓編譯器知道要顯示什麼Object method或attribute
#就可以不需要背那麼多指令
#List使用方法：List[object]
#List意義：說明陣列中元素的資料型態
#Union使用方法：Union[object1,object2,...]
#Union意義：型態的「集合」，就是裡面會有各種不同的型態
list1:List[Union[str,int,float]] = [1,'abc',3.7]
```

陣列的各種功能：   
首先先了解Class method(類別功能)  
`object().func()`  
就是一個`class`中自帶的功能  

```python
list1 = [3,2,1,3,4,2,7,1,10]

#=====插入元素=====

list1.append(3)
#在陣列尾端插入3的元素

list1.insert(3,5)
#在陣列索引值為3的地方插入5的元素

#=====刪除元素=====

list1.pop(3)
#刪除索引值為3的元素

list1.remove(4)
#刪除由左到右第一個出現4的元素

#=====陣列內建函數=====
#陣列長度函數：
len(list1)

#陣列最大值：
max(list1)

#陣列最小值
min(list1)


#=====其他功能=====
#反轉陣列：
list1.reverse()

#將陣列的數值做排序
list1.sort()
#(不推薦使用因為速度太慢)
#詳情參考排序法
#快速排序法&氣泡排序法
#(推薦自己寫quicksort)
```

### 元組`Tuple`
我都叫他數對  
```python
tuple1 = ('e', 2.7182818, '黃金比例', 1.618)
```

跟陣列幾乎一樣，但是是小括號的  
通常使用在將具有對應關係的資料包起來  

> 不能修改元素(不會造成資料遺失)
> 執行速度快

### 基本輸出輸入(I/O)(input/output)
輸出`print()`  
語法：  
`print(object)`
功能：在終端機上輸出文字  
比如：  
```python
print('Hello world')
print(1+1)
print('1'+'1')
print()
print(type(1/3))
print('1','2')
```
執行結果：  

結果說明：  
第一行為直接輸出字串  
第二行為輸出`1+1`的結果  
第三行為輸出兩字串`'1','1'`的相加結果   
第四行為輸出空行  
第五行為輸出$\dfrac{1}{3}$在`python`中的型態  
第六行為輸出`'1'`和`'1'`中間使用空格隔開  
![](https://i.imgur.com/JFcGym1.png)  
 
> 逗點即為分開輸出  
> 字串與字串間能相加但不能相減   
> 字串是一種陣列(`list`)  

 
輸入`input()`  
語法：`input(str)`  
比如：  
```python
a=input('輸入身高(公分)\n')
a=float(a)/100#轉換為數值型態才能與數字做運算
print('你的身高為'+str(a)+'公尺')
```  
![](https://i.imgur.com/4etcls6.png)

> `input()`括弧中若沒有填入字串，則不會輸出任何東西  
> `input()`會等到使用者輸入字詞時才結束  

功能：回傳使用者在終端機上的輸入(回傳型態為str)  

條件句`if,elif,else`  
語法：  
```python
condition1 = (1==1)and(2<=3)
condition2 = #...
if condition1:bool:
    #...
elif condition2:bool:
    #...
else:
    #...
```
功能：  
一組`if-elif-else`由上到下檢驗  
1. 若第`n`個條件未成立，則判斷第`n+1`個條件是否成立。  
2. 只要有一條件成立，則只執行其條件內的敘述，不執行其他的敘述。  
3. 若所有條件句都為假，則在存在`else`的前提下執行`else`的內容(default function)。
4. `elif`、`else`皆為optional。
5. `elif`可以有無窮多個
 
比如：   
```python
a = 50
b = 30
if a+b <= 100:
    a=a+2
    b=b*2
elif a+b <= 80:
    a=3
    b=2
else:
    a=7
    b=0
    
print(a,b)
```

結果說明：  
因為在第一行中，`a+b<=100`已經成立，故執行`if`內的敘述之後  
跳到輸出`a,b`  
因此結果為52 60  
![](https://i.imgur.com/aPhO4Qy.png)  

實作：  

範例1：簡易加法計算機  

題目敘述：  

輸入有一行，包含兩個整數$-2^{32}<a<2^{32}$與$-2^{32}<b<2^{32}$，一個運算符號$+$

輸出其數學上的結果

範例輸入：1+1

範例輸出：2

參考解答：  
```python
a=0
b=0
data = input()
data = data.split('+')
a=int(data[0])
b=int(data[1])
print(a+b)
```
> 字串型態有一個功能叫做`.split(str)`    
> 其功能為：在字串中尋找括弧內的字元，以之為中心將字串分解成兩個部分  
> 例如  
> ```python
> string = '1986-06-04'
> string = string.split('-')
> print(string)
> ```
> ![](https://i.imgur.com/W7xEcE0.png)  
> 其輸出為一陣列  
> 如果沒有括弧中的字元則會回傳一個`list`  
> 其中只有一個元素為原本的字串  

範例2：計算BMI  
題目敘述：給定兩數h與w分別代表身高(公尺)與體重  
輸出其BMI值，並四捨五入至小數點後2位  
(BMI=$\dfrac{w}{h^2}$)  
 
參考解答：  
```python
h = input()
w = input()
h = float(h)
w = float(w)
bmi = w/(h*h)
print(round(bmi,2))
```

範例3：  


範例4：解一元二次方程式  
題目敘述：給定3數$a,b,c$代表$ax^2+bx+c$，輸出$ax^2+bx+c=0$的解  

---
### 演算法

演算法並沒有想像中的那麼可怕，它只是利用固定的運算模式  
將某些輸入會對應某些輸出  
其實就是程式設計師設計的一種函數  
以下是演算法的基礎語法  

### 迴圈：

迴圈分為`for`迴圈與`while`迴圈  

`for`迴圈  
語法：  
```python
for var in iterable_object:
    #...
```

功能：  
將`in`後方的`iterable`(能夠迭代的物件)將其元素逐一取出存入`var`  
`var`是可以自行取名的變數  

`iter`的說明請參考這篇  
https://vivi.emmphysics.com/%E6%90%9E%E6%B8%85%E6%A5%9Apython%E4%B8%AD%E7%9A%84iterable%E3%80%81iterator%E5%92%8Cgenerator%EF%BC%88%E4%B8%80%EF%BC%89/  
> 典型的`iter`物件就是陣列  
> 事實上`str,tuple,dict`都可以視為陣列的一種，等等會再提到  



常與`for`迴圈使用的函數  
```python
range(start:int,stop:int,step:int)  
#start and step is optional(選填參數)
#start has a default value of 0(預設值為0)
#step has a default value of 1(預設值為1)
#range()是一個物件，他會回傳一個陣列
#例如range(0,5)->[0,1,2,3,4]
enumerate(sequence:iter[,start:int = 0])
```
`enumerate()`功能說明  
```python
list1 = ['a','b','c']
print(list(enumerate(list1)))
```
![](https://i.imgur.com/6JAu2ir.png)  
就是將每個元素變成`(index,object)`的`tuple`形式  

比如：  
計算  
$\displaystyle\sum_{k=1}^{30}(2k-1)=?$

```python
sum = 0
for i in range(30):
    sum += 2*(i+1)-1
```

範例5：氣泡排序法  

範例6：https://zerojudge.tw/ShowProblem?problemid=a216  

範例7：判斷是否為整數  




> 小技巧：在不知道程式哪邊出問題時可以`print()`各種參數或是字串       
> 例如：想要輸出`foo(1)`為3卻沒有反應    
> ```python
> def foo(x):
>     if x>1:
>         return 2
>     elif x<1:
>         return 3
> print(foo(1))
> ```
> 將不會輸出任何東西  
> 因此在各個if-elif判斷式中加上`print(...)`確認是跑進哪個條件式中  
> 在最外面也加上`print(...)`以確認有執行`foo()`函式  
> ```python
> def foo(x):
>     print('a')
>     if x>1:
>         print('b')
>         return 2
>     elif x<1:
>         print('c')
>         return 3
> print(foo(1))
> ```
> 輸出理論上要有一個a和一個c，但卻只有輸出a，表示`elif x<1:`這個判斷式有問題  
> 因此修改為`elif x<=1:`則程式就可以正常運行了。  


### 物件Object


物件的概念：  
生活中每個東西都有自己的功能與屬性(通常為外觀)  
以下拿手機作為舉例  
比如手機可以打電話、玩遊戲、看影片、聽音樂。這樣的「功能」可以對應到程式設計中「物件方法(method)」的概念。  
而手機可以自己設定桌面背景、選擇手機顏色、要不要加上手機殼或是配件。這樣能夠做更改的變數對應到程式設計中「物件屬性(attribute)」的概念。  

在`python`中，物件的宣告通常是使用`class`關鍵字

中文名稱為「類」

範例：

```python
class Smartphone:
    def __init__(self, shell = None, color = 'white', desktop_image = 'image.png'):
        #物件的初始化函數
        #(init stands for initialize)
        #當物件產生時會被執行
        #通常是設定參數
        self.shell = shell
        self.color = color
        self.desktop_image = desktop_image
        self.user_name = 'Steve'
        self.number = '09123456781'
        self.internet_connected = True
    
    def call_someone(self, contactant):
        #宣告物件方法(也是一種函數，只是只能透過這個物件存取)
        #self是用以存取本身資料的一個參數
        #透過self能夠存取到目前當下物件的各種狀態
        call(contactant.number)
        
    def play_game(self, game):
        game_open(game)
        game.run()
    
    #...
    
#產生物件
phone1 = Smartphone(shell = '犀牛盾', color = 'black', desktop_image = 'default.png')        

#使用物件方法
phone1.call_someone(contactant = 'Alex')

#改變物件屬性
phone1.user_name = 'John'
phone1.desktop_image = 'Rickroll.png'
```
使用物件的話就可以大量生產製造重複的東西，但又保有能夠客製化的選項。

因為產生物件時只能使用其對外公開的參數與功能，物件的內部函數是如何寫的也能保有隱蔽性，不易被抄襲。

`class`對程式的速度影響非常小，且能夠增加程式可讀性，也因此在寫大型`project`時通常都會使用大量的物件，也就發展出了所謂的「物件導向」程式，例如`Java, JavaScript`。

#### 子類subclasses
有些物件具有大量的屬性，這時候就可以使用子類來將「具有相同特性的屬性」分類
這也能夠大幅提升程式的可讀性。

範例：
```python
class MySqlDataBase:
    class SqlInfo:
    #此即子類，設定MySql執行時需要使用的各種參數
        def __init__(self, host, user, password, database):
            self.host = host
            self.user = user
            self.password = password
            self.database = database
    
    def __init__(self):
        self.SqlInfo.host = host
        self.SqlInfo.user = user
        self.SqlInfo.password = password
        self.SqlInfo.database = database
        #雖然現在看起來創建子類並沒什麼意義，但是也許之後會加上其他屬性，因此先保留著

    def connect_to_db(self):
        db = mysql.connector.connect(
            host = self.SqlInfo.host,
            user = self.SqlInfo.user,
            password = self.SqlInfo.password,
            database = self.SqlInfo.database
            )
        return db 

    def get_db_data(self, sql_cmd:str, values:tuple = ()):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute(sql_cmd, values)
        return cursor.fetchall()

    def insert_data(self, sql_cmd:str, values:tuple):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute(sql_cmd, values)
        return db.commit()

    def del_data(self, sql_cmd:str, values):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute(sql_cmd, values)
        return db.commit()
    
    def update_data(self, sql_cmd:str, values:tuple):
        db = self.connect_to_db()
        cursor = db.cursor()
        cursor.execute(sql_cmd, values)
        return db.commit()
```






