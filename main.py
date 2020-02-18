import random


class Gamer:
    """Игрок.

     """
    def __init__(self):
        self.card = random.sample(range(10, 99), 5)
        self.name = "Gamer"

    def __str__(self):
        return self.name


class Master(Gamer):
    """ Ведущий. Наследуется от игрока.
    """
    bag = range(10, 101)  # мешок с бочонками
    numbers_out = []  # выбывшие бочонки

    def __init__(self):
        super().__init__()
        self.name = "Master"

    def new_number(self):
        """ Взятие нового бочонка из мешка
        и добавление в стек использованных
        """
        while self.bag:
            number = random.choice(self.bag)  # берем бочонок из мешка
            yield number
            self.numbers_out.append(number)  # добавляем в использованные бочонки

    @staticmethod
    def check_cards(*args):
        args = master_card, gamer_card
        if master_card != gamer_card:
            print(f"Карточка игрока {gamer} : ", master_card)
            print(f"Карточка ведущего {master}: ", gamer_card)
            return True


def main():
    """ Ход игры
    """

    if master.check_cards(master_card, gamer_card):  # если карточки уникальны

        for number in gen_new_n:  # берем бочонок
            print(f"Бочонок {number}")
            for object in (gamer, master):  # для обоих игроков проверяем, есть ли такая цифра
                if object.card == ["*", "*", "*", "*", "*"]:
                    print(f"--------------------------\nИгрок {object} победил!\n--------------------------")
                    return True
                else:
                    for index, element in enumerate(object.card):  # для индекса и числа в карточке
                        if element == number:
                            object.card[index] = "*"
                            print(f"Икрок {object} зачеркнул цифру {number}")

            continue

        print('Бочонки закончились')


    else:
        print("Игру нужно начать сначала")


if __name__ == "__main__":
    gamer = Gamer()  # новый игрок
    master = Master()  # новый ведущий
    gamer_card = gamer.card  # карточка игрока
    master_card = master.card  # карточка ведущего
    gen_new_n = master.new_number()  # создаем генератор (мешок)
    main()
    print(f"Результаты игры:\nкарточка игрока {gamer} {gamer_card}\n"
          f"карточка игрока {master} {master_card}")