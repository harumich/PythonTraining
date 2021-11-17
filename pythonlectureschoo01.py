#1-100を足した合計を計算しなさい
 #とりあえずの解答例Python
i, total = 1, 0
while i <= 100:
    total += i
    i += 1

print(total)
 #少し工夫した解答例
print(sum(range(1, 101)))


#1-1000のうち7もしくは１で割り切れる数の合計を計算してください
 #とりあえずの解答例
total = 0
for i in range(1, 1001):
    if i % 7 ==0 or i % 13 ==0:
        total += i
print(total)

 #少し工夫した解答例
print(sum(i for i in range(1, 1001) if i % 7 == 0 or i % 13 == 0))


#whileとelseの組み合わせ
lst = [1, 9, 19, 5, 7]
for elem in lst:
    if elem % 2 == 0:
        print('{}は偶数です'.format(elem))
        break
else:
    print('偶数は見つかりませんでした')


#クラスでのアンダースコア
class MyClass:
    def __init__(self):
        self.x = 1
        self._x = 2       #"_XXX"は「名前を隠したい」という意思表示
        self.__x = 3      #"__xxx"は「名前を隠したい」という意思表示＋（クラスで）名前のマンぐリングが発生する
o = MyClass()
print(o.x)            #1
print(o._x)           #2
print(o._MyClass__x)  #3  #継承したときに衝突しないため（javaのprivateのような「隠す」機能はない）

#__xxx__(Dunder)について
lst = [1, 2, 3, 4, 5]

print(lst[1:3])
print(lst.__getitem__(slice(1,3))) #Dunderは勝手にユーザーが定義してはいけない
                                   #舞台裏には__xxx__()あり→len(o)＝o.__len__(),o[x]＝o.__getitem__(x)


#for文をwhile文で書くと
total = 0
for i in range(1, 101):
    total += i
print(total)  #5050

total = 0 
my_iterator = iter(range(1, 101))
try:
    while True:
        i = next(my_iterator)
        total += i
except StopIteration:
    pass
print(total)  #5050