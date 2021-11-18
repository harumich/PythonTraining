# クラス変数とインスタンス変数

class Rectangle:
    recs = []  #クラス変数（__init__メソッドの外で定義する・クラスインスタンス間でデータ共有）

    def __init__(self, w, l):
        self.width = w  #インスタンス変数
        self.len = l    #インスタンス変数
        self.recs.append((self.width, self.len))
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

r1 = Rectangle(10, 24)
r1 = Rectangle(20, 40)
r1 = Rectangle(100, 200)

r1.print_size()  #[オブジェクト名].[クラスメソッド名] or [インスタンス名].[クラスメソッド名] で入力

print(Rectangle.recs) #クラス変数は　[クラス名].[クラス変数]　で使う。


#特殊メソッド
 #__repr__の例
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)

 #__add__の例
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)   #absは組み込み関数で絶対値を取る

x = AlwaysPositive(-20)
y = AlwaysPositive(10)
print(x + y)


#is 

x = 10
if x is None:
    print("x はNone")
else:
    print("x はNoneじゃない")

x = None
if x is None:
    print("x はNone")
else:
    print("x はNoneじゃない")