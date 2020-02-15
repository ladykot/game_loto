import random


class Gamer:
    """Игрок.

     """
    def __init__(self):
        self.card = []
        self.name = "Gamer"

    def __str__(self):
        return self.name

    def new_card(self):
        """ генерация карточки из 5 уникальных двузначных чисел """
        for n in range(5):
            if n in []:
                continue
            self.card.append(random.randrange(10, 99, 1))
        return self.card

    def check_number(self, card, number):
        """ Проверка бочонка.
            Eсли число есть в карточке каждого игрока,
            помечаем его *

        """
        self.card = card
        for index, element in enumerate(self.card):
            if element == number:
                self.card[index] = "*"
                print(f"Бочонок номер {number} в карточке {self.name}")
                return True
            else:
                return False


class Master(Gamer):
    """ Ведущий. Наследуется от игрока.
    """
    bag = [_ for _ in range(10, 101)]  # мешок с бочонками
    numbers_out = []  # выбывшие бочонки

    def __init__(self):
        Gamer.__init__(self)
        self.name = "Master"

    def new_number(self):
        """ Взятие нового бочонка из мешка
        и добавление в стек использованных
        """
        random.shuffle(self.bag)  # перемешиваем бочонки
        while self.bag:
            number = self.bag.pop()  # берем бочонок из мешка
            yield number
            self.numbers_out.append(number)  # добавляем в использованные бочонки

    @staticmethod
    def check_cards(*args):
        args = master_card, gamer_card
        if master_card != gamer_card:
            print(f"Карточка игрока {gamer} : ", master_card)
            print(f"Карточка ведущего {master}: ", gamer_card)
            return True


gamer = Gamer()  # новый игрок
master = Master()  # новый ведущий
gamer_card = gamer.new_card()  # карточка игрока
master_card = master.new_card()  # карточка ведущего