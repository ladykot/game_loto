from game_loto.start import master, gamer, master_card, gamer_card
from game_loto.apps_folder.main_game import main


if master.check_cards(master_card, gamer_card):  # если карточки не уникальны
    main()
    print(f"Результаты игры:\nкарточка игрока {gamer} {gamer_card}\n"
          f"карточка игрока {master} {master_card}")
else:
    print("Игру нужно начать сначала")
