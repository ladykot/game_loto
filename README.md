## Написать игру "Лото"
### Реализуйте имитацию игры в лото.


**Первый объект — ведущий.**

У ведущего 2 стека чисел.
1 - числа, которые могут участвовать в следующем розыгрыше
2 - выбывшие числа

Ведущий умеет проверять билеты на честность, вытаскивать следующее число и выдавать новые билеты

**Второй объект — игрок**

В начале игры ведущий выдает вам карточку, которая хранит 5 случайных двузначных числа. Карточки не должны повторяться.

При следующем выводе числа, вы помечаете у себя в билете выпавший номер, если у вас он есть.

Игра продолжается, пока один из игроков не соберет все числа в билете

    
## Запуск

Игра запускается в коммандной строке:

    python main.py
    