from libre.Card import Card
from libre.Chips import Chips
from libre.Deck import Deck
from libre.Hand import Hand


def checker(question):
    temp = input(question)
    while temp not in ['y', 'n']:
        print("Некорректный ввод!")
        temp = input()
    return temp


def comp_wins():
    print("Компьютер победил!")
    bank.lose_bet()


def player_wins():
    print("Вы победили!")
    bank.win_bet()


m_answer = checker("Black Jack.\nВы готовы начать игру?(y/n)\n")
if m_answer == 'y':
    bank = Chips()
    print("Введите размер банка:")
    while type(bank.total) != float or bank.total <= 0:
        try:
            bank.total = float(input())
            if bank.total <= 0:
                print("Величина банка положительна!")
        except ValueError:
            print("Некорректный ввод!")
            continue
while m_answer == 'y':
    if bank.total == 0:
        print("Вы банкрот! С вами никто не хочет играть.")
        m_answer = 'n'
        continue
    print(f"Ваш банк: {bank.total}")
    playing = True
    comp_turn = False
    player = Hand()
    computer = Hand()
    deck = Deck()
    deck.shuffle()

    print("Введите размер ставки:")
    while type(bank.bet) != float or bank.bet <= 0 or bank.bet > bank.total:
        try:
            bank.bet = float(input())
            if bank.bet <= 0:
                print("Размер ставки положителен!!")
        except ValueError:
            print("Некорректный ввод!")
            continue
        if bank.bet > bank.total:
            print("Ставка больше банка!")
    print("\n"*100)
    print("Партия началась!\n")
    for i in range(0, 4):
        if i % 2 == 0:
            player.add_card(deck.deal())
        else:
            computer.add_card(deck.deal())
    while playing:
        if not comp_turn:
            print(f"Карты компьютера:\n<Карта скрыта>\n{computer.show()[1]}")
        else:
            print("Карты компьютера:\n" + '\n'.join(computer.show()))
            print(f"Количество очков компьютера:{computer.value}")
        print("\nВаши карты:\n" + '\n'.join(player.show()))
        print(f"Ваше количество очков:{player.value}")
        if not comp_turn:
            answer = checker("Возьмете еще карту?(y/n)\n")
            if answer == 'y':
                player.add_card(deck.deal())
                print(f"Ваше количество очков:{player.value}")
                if player.aces > 0:
                    answer = checker("Сменить стоимость туза?(y/n)\n")
                    if answer == 'y':
                        player.adjust_for_ace()
                    print(f"Ваше количество очков:{player.value}")
                if player.value > 21:
                    playing = False
                    comp_wins()
                    print("Карты компьютера:\n" + '\n'.join(computer.show()))
                    print("\nВаши карты:\n" + '\n'.join(player.show()))
            else:
                comp_turn = True
        else:
            input("Нажмите любую клавишу для хода компьютера: ")
            if player.value >= computer.value < 21:
                print(1)
                computer.add_card(deck.deal())
                if computer.value > 21:
                    playing = False
                    player_wins()
                    print("Карты компьютера:\n" + '\n'.join(computer.show()))
                    print("\nВаши карты:\n" + '\n'.join(player.show()))
            else:
                playing = False
                comp_wins()
                print("Карты компьютера:\n" + '\n'.join(computer.show()))
                print("\nВаши карты:\n" + '\n'.join(player.show()))

