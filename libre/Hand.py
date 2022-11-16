from libre import Card


class Hand:
    values = {'Двойка': 2, 'Тройка': 3, 'Четвёрка': 4, 'Пятерка': 5, 'Шестёрка': 6, 'Семёрка': 7,
              'Восьмёрка': 8, 'Девятка': 9, 'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.values[card.rank]
        if card.rank == 'Туз':
            self.aces += 1

    def adjust_for_ace(self):
        if self.aces > 0:
            self.aces -= 1
            self.value -= 10

    def show(self):
        str_ret = ""
        ret = []
        for i in self.cards:
            ret.append(i.__str__())
            str_ret = "\n".join(map(str, ret))
        return ret

