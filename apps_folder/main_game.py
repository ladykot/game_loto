from game_loto.start import master, gamer, master_card, gamer_card


def main():
    """ Ход игры
    """
    gen_new_n = master.new_number()  # создаем генератор (мешок)

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






