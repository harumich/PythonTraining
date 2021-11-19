#戦争（トランプゲーム）

from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9",
               "10", "Jack", "Queen","King", "Ace"]

    def __init__(self, v, s):
        """スート（マーク）も値も整数値です"""
        self.value = v
        self.suit = s

    def __it__(self, c2):
        if self.value < c2.value:
            return True
        
        if self.value == c2.value:                     
            #if self.suit < c2.suit:
                #return True
            #else:
                #return False　　を一行にまとめたのが次のコード
            return self.suit < c2.suit
        return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            #if self.suit > c2.suit:
                #return True
            #else:
                #return False　　を一行にまとめたのが次のコード
            return self.suit > c2.suit
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " +self.suits[self.suit]
        return v

card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 > card2)
print(card1 < card2)

card = Card(3, 2)
print(card)


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()  # pop()：指定した位置の要素を削除し、値を取得

deck = Deck()
for card in deck.cards:
    print(card)


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("プレイヤー１の名前：")
        name2 = input("プレイヤー２の名前：")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = "このラウンドは {} が勝ちました！".format(winner.name)
        print(w)

    def print_draw(self, p1, p2):
        d = "{} は {}、{} は {} を引きました".format(p1.name, p1.card, p2.name, p2.card)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            response = input("q で終了、それ以外のキーでPlay：")
            if response == "q":
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        if win == "引き分け！":
            print(win)
        else:
            print("ゲーム終了、{} の勝利です！".format(win))

    def winner(self, p1, p2):
        if self.p1.wins > self.p2.wins:
            return self.p1.name
        if self.p1.wins < self.p2.wins:
            return self.p2.name
        return "引き分け！"

game = Game()
game.play_game()
