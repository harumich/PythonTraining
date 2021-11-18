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
