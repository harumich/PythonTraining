#オブジェクト指向プログラミング

class Orange:                       #クラス名は最初大文字・区切りは頭文字を大文字に
    def __init__(self, w, c):       #スイート部分：__init__は特殊メソッド、ここで必須の第一引数はselfで、self関数はインスタンス関数の定義に使う。
        """weight(重さ)はグラム"""   #__init__は初期化の特殊メソッド
        self.weight = w             #selfとその他の引数をつなげる
        self.color = c              #weightとcolorはインスタンス変数
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """temp(温度)は摂氏"""
        self.mold = days * temp

orange = Orange(200, "dark orange")     #クラスのインスタンス化
print(orange.weight)                   #[オブジェクト名].[インスタンス変数名]
print(orange.color)
print(orange.mold)

orange.rot(10, 37)                     #このクラスのオブジェクト専用のメソッド
print(orange.mold)



#別の例
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len
    
    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())