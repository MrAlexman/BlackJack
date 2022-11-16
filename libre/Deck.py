import random
from libre import Card


class Deck:
    suits = ('Червы', 'Бубны', 'Пики', 'Трефы')
    ranks = ('Двойка', 'Тройка', 'Четвёрка', 'Пятерка', 'Шестёрка', 'Семёрка',
             'Восьмёрка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз')

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card.Card(suit, rank))

    def __str__(self):
        str_ret = ''
        ret = []
        for i in self.deck:
            ret.append(i.__str__())
            str_ret = "\n".join(map(str, ret))
        return str_ret

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
