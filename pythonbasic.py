#行

print("""これは、とても、とても、
      とても、とても長い複数行の
      コードです。""")

print\
("""これは、とても、とても、とても、
とても長い複数行のコードです。""")


#関数
 #引数が1つ
def  f(x):
    return x + 1

z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")

 #引数がない
def f():
    return 1 + 1
result = f()
print(result)

def f():
    z = 1 + 1 #メソッド（機能）を持っていない！
result = f()
print(result)  #Noneが表示（returnがないと）

 #引数が複数
def f(x, y, z):
    return x + y + z
result = f(1, 2, 3)
print(result)


#関数を再利用する
def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")

even_odd()
even_odd()
even_odd()


#必須引数とオプション引数
 #オプション引数の例①
def f(x=2):
    return x ** x
print(f())   #デフォルトでx=2
print(f(4))  #x=4が引数になる

 #オプション引数の例②
def add_it(x, y=10):
    return x + y

result = add_it(2)
print(result)


#グローバル関数とローカル関数
x = 100

def f():
    global x #「global」で関数内からでもグローバル変数の更新が可能
    x += 1
    print(x)
    
f()

#例外処理
 #0で割れないの例外処理
a = input("type a number")
b = input("type another")
a = int(a)
b = int(b)
try:
    print(a/ b)
except ZeroDivisionError:
    print("b cannot be zero.")


 #0で割れないの例外処理＋数字が入っていない例外処理
try:
    a = input("type a number")
    b = input("type another")
    a = int(a)
    b = int(b)
    print(a/ b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")


#ドキュメンテーション文字列
def add(x, y):
    """
    Returns x + y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    return x + y


#メソッド（メソッドと関数は引数を用いる点では似ているが、メソッドはオブジェクトの後ろにつけて呼び出します。）
print("Hello".upper())

print("Hello".replace("o", "@"))


#リスト
 #1 
fruit = list()
 #2
fruit = []
 #3
fruit = ["apple","orange","pear"]
 
 #リストの追加
fruit = ["apple","orange","pear"]
fruit.append("banana")
fruit.append("peach")  #['apple','orange','pear','banana','peach']

 #インデックス値
fruit = ["apple","orange","pear"]
fruit[0]  #'apple'
fruit[1]  #'orange'
fruit[2]  #'pear'

 #リストの結合
colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
colors = colors1 + colors2  #['blue','green','yellow','orange','pink','black']
len(colors)  #6

 #リスト内の検索
colors = ["purple", "orange", "green"]

guess = input("何色でしょうか？：")

if guess in colors:
    print("あたり！")
else:
    print("はずれ！")


#タプル(タプルを一度作成したら、要素の追加・更新ができません)
 #1
my_tuple = tuple()  #()
 #2
my_tuple = ()  #()
 #3
rndm = ("M.Jackson", 1958, True)  #('M.Jackson', 1958, True)

 #検索
rndm = ("M.Jackson", 1958, True)
rndm[2]   #True


#辞書
 #1
my_dict = dict()
 #2
my_dict = {}
 #3
fruits = {"Apple": "Red",
          "Banana": "Yellow"}  #{'Apple': 'Red', 'Banana': 'Yellow'}

 #バリューの追加とキーで参照
facts = dict()

facts["code"] = "fun"  #バリューを追加

facts["code"]   #キーで参照

facts["founded"] = 1776  #バリューを追加

facts["founded"]   #キーで参照

 #キーバリューペアを辞書から削除
books = {"Dracula": "Stoker",
         "1984": "Orwell",
         "The Trial": "Kafka"}

del books["The Trial"]

books  #{'Dracula': 'Stoker', '1984': 'Orwell'}


#辞書バリューとして、リスト・タプル・辞書を格納
ny = {
    "座標": (40.7128, 74.0059),

    "セレブ": [
        "ウッディ・アレン",
        "ジェイ・Z",
        "ケヴィン・ベーコン",
    ],

    "事実": {
        "州": "ニューヨーク",
        "国": "アメリカ",
    }
}







