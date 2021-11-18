#オブジェクト指向型プログラミング（４大要素）

#カプセル化 (pythonはすべてパブリック変数なのでアンダーバーを使う)
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # client が使っても良い
        pass

    def _unsafe_method(self):
        # client は使うべきではない（自己責任）
        pass


#抽象化


#ポリモーフィズム (同じインターフェースでありながらデータ型に合わせて異なる動作をする機能)
  #インターフェース＝関数やメソッド
#例１(print関数)
print("Hello, World!") #str型を使っている
print(200)             #int型を使っている
print(200.1)           #float型を使っている


#例２(2パターンの比較)

#ポリモーフィズムなしで様々な形状を描写する場合
"""
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if isinstance(a_shape, Triangle):
        a_shape.draw_triangle()
    if isinstance(a_shape, Square):
        a_shape.draw_square()
    if isinstance(a_shape, Circle):
        a_shape.draw_circle()

#ポリモーフィズムを実装して描写する場合（ダック・タイピング）
shapes = [tr1, sw1, cr1]
for a_shape in shapes:
    a_shape.draw()

"""
#継承
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len   #子クラス独自のメソッド

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))   #メソッドオーバーライド（親クラスのメソッドの上書き）

a_square = Square(20, 20)
print(a_square.area())
a_square.print_size()


#コンポジション（別クラスのオブジェクトを変数として持たせる）
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)  #別クラスのオブジェクトを変数として持たせる
print(stan.owner.name)
