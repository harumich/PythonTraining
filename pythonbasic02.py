#インデックス
author = "Kafka"
print(author[0])   #K
print(author[1])   #a
print(author[-1])  #a
print(author[-3])  #f

#formatメソッド
what = input("何が：")
when = input("いつ：")
where = input("どこで：")
do = input("どうした：")

r = "{}は{}に{}で{}。".format(what, when, where, do)
print(r)   #ブタは今日に家でエサを食べた。


#改行
print("line1\nline2\nline3")

#スライス
ivan = "死の代わりにひとつの光があった。"
print(ivan[0:6])   #死の代わりに
print(ivan[6:16])  #ひとつの光があった。
print(ivan[:6])    #死の代わりに
print(ivan[6:])    #ひとつの光があった。


#forループ
 #文字列
name = "Ted"
for character in name:
    print(character)

 #リスト
shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)

 #辞書
people = {"G. Blith II": "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny",
          }

for character in people:
    print(character)


 #forループを使ってリストなどのミュータブルなイテラブルを更新(インデクス関数iを追加してくれるenumerate関数)
tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

 #range
for i in range(1, 11):
    print(i)


#whileループ
x = 10 
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

#whileループ（無限ループ）
while True:
    print("Hello, world!")

#break文
for i in range(0, 100):
    print(i)
    break     #0

#continue文(実行中の反復処理を途中で終了して、次なる反復処理を実行する)
for i in range(1, 6):      #1
    if i == 3:             #2
        continue           #4
    print(i)               #5


#モジュール(モジュール名.｛変数　or 関数})
import math 

math.pow(2, 3)


#他のモジュールにインポートする(動作確認用のテストコードが書かれている場合の防止方法)
 #通常例（関数）
def print_hello():     #module1.pyで　"  "
    print("Hello!")

import hello
hello.print_hello()    #module2.pyで　Hello!
 
 #ダメ例
print("Hello!") #module1.pyで　Hello!

import module1  #module2.pyで Hello!(やりたくもないのに)

 #良い例(動作確認用のテストコードが書かれている場合の防止方法)
if __name__ == "__main__":    #module1.pyで　Hello!　
    print("Hello!")

import module1     #module2.pyで　" "





