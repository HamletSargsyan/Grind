import os

os.system("clear")

text = [
    """Секунды   : 9,999,999,999,999 | Профиль : Catalyst
Минуты    : 282               | Уровень : 2,390
Часы      : 2                 | Доллары : 523,421,432,234$

< Ресурсы >

Камень    : [######....] 60%  | \033[32ml: 1000\033[0m | 134$
Дерево    : [###.......] 30%  | \033[32ml: 1111\033[0m | 2,340$
Уголь     : [###.......] 300% | \033[32ml: 10\033[0m   | 100,345$
Ткань     : [..........] 1%   | \033[32ml: 56\033[0m   | 50,345$
Медь      : [#######...] 75%  | \033[32ml: 1\033[0m    | 10,350$ 
Железо    : [########..] 89%  | \033[31ml: 122\033[0m  | 20,345$
Золото    : [#.........] 1%   | \033[32ml: 9999\033[0m | 303,450$
Уран      : [##########] 100% | \033[32ml: 2\033[0m    | 981,923,324,000,000,000,000$
Кремнелит : [##........] 100% | \033[31ml: 220\033[0m  | 18,031,324$

Действие  : 
""",
    """Секунды   : 9,999,999,999,999 | Профиль : Catalyst
Минуты    : 282               | Уровень : 2,390
Часы      : 2                 | Доллары : 523,421,432,234$

< Цвета >

█ Белый краситель           1 \033[0m| ███████ | max   | 
\033[2m█ Серый краситель           2 \033[0m| \033[2m███     \033[0m| 24 ч  |
\033[31m█ Красный краситель         3 \033[0m| \033[31m██      \033[0m| 48 ч  |
\033[33m█ Желтый краситель          4 \033[0m| \033[33m█       \033[0m| 72 ч  |
\033[32m█ Зелёный краситель         5 \033[0m| \033[32m█████   \033[0m| 96 ч  |
\033[36m█ Бирюзовый краситель       6 \033[0m| \033[36m██      \033[0m| 120 ч |
\033[34m█ Синий краситель           7 \033[0m| \033[34m█       \033[0m| 144 ч |
\033[35m█ Фиолетовый краситель      8 \033[0m| \033[35m        \033[0m| 168 ч |

Действие  : 
""",
    """Секунды   : 9,999,999,999,999 | Профиль : Catalyst
Минуты    : 282               | Уровень : 2,390
Часы      : 2                 | Доллары : 523,421,432,234$

< 5. Медь >

Колличество : 21,840 
Хранилище   : 145,816 
Стоимость 1 : 888$ 
В секунду   : 22.4 
Уровень     : 220 

Улучшение
\033[32m
Хранилище   : +330
Стоимость 1 : +4
В секунду   : +0.1

Цена улучшения : 53,370,760$
Доллары        : 338,791,019$
\033[0m
Действие  : 
""",
    """Секунды   : 9,999,999,999,999 | Профиль : Catalyst
Минуты    : 282               | Уровень : 2,390
Часы      : 2                 | Доллары : 523,421,432,234$

< Достижения >
 ________
|   _    | 1. Спустя час
|  / |   | Получить 1 уровень
|    |   |
|  ‾‾‾‾  |
 ‾‾‾‾‾‾‾‾
 ________
|   _    | 2. Ветки
|  <`)   | Открыть дерево
|  ( \_  |
|   ""   |
 ‾‾‾‾‾‾‾‾

""",
    """Секунды   : 9,999,999,999,999 | Профиль : Catalyst
Минуты    : 282               | Уровень : 2,390
Часы      : 2                 | Доллары : 523,421,432,234$

< Магазин >

1. Железный доспех - 320 минут
2. Осадочная порода - 31 минут
3. Кремнелитовый меч - 5,000 минут
4. Свинцовая стружка - 10 минут
""",
    """Секунды   : 9,999,999,999,999 | Профиль : C
Минуты    : 282               | Уровень : 2,390
Часы      : 2                 | Доллары : 523,421,432,234$

Ресурсы

Камень    : [..........] 0%   | \033[32ml: 1000\033[0m | 134$
Дерево    : [###.......] 30%  | \033[32ml: 1111\033[0m | 2,340$
Уголь     : [###.......] 300% | \033[32ml: 10  \033[0m | 100,345$
Ткань     : [..........] 1%   | \033[32ml: 56  \033[0m | 50,345$
Медь      : [#######...] 75%  | \033[32ml: 1   \033[0m | 10,350$ 
Железо    : [########..] 89%  | \033[32ml: 122 \033[0m | 20,345$
Золото    : [#.........] 1%   | \033[31ml: 9999\033[0m | 303,450$
Уран      : [##########] 100% | \033[31ml: 2   \033[0m | 981,923,324,000,000,000,000$
Кремнелит : [##........] 100% | \033[31ml: 220 \033[0m | 18,031,324$
Хром      : [..........] 0%   | \033[31ml: 10  \033[0m | 26,000,369$

Красители

█ Белый краситель             \033[0m| \033[31ml: 10  \033[0m | 500,000,000$ / c
\033[2m█ Серый краситель             \033[0m| \033[31ml: 25  \033[0m | 853,836,825,285$ / c 
\033[31m█ Красный краситель           \033[0m| \033[31ml: 1   \033[0m | 100,000,000$ / c 
\033[33m█ Желтый краситель            \033[0m| \033[32ml: 2   \033[0m | 500,000,000$ / c   
\033[32m█ Зелёный краситель           \033[0m| \033[31ml: 13  \033[0m | 1,000,000,000$ / c
\033[36m█ Бирюзовый краситель         \033[0m| \033[31ml: 19  \033[0m | 10,000,000,000$ / c
\033[34m█ Синий краситель             \033[0m| \033[32ml: 162 \033[0m | 50,000,000,000$ / c
\033[35m█ Фиолетовый краситель        \033[0m| \033[32ml: 276 \033[0m | 100,000,000,000$ / c
\033[0m░ Черный краситель            \033[0m| \033[32ml: 276 \033[0m | 100,000,000,000$ / c
\033[0m▒ Блестки                     \033[0m| \033[32ml: 276 \033[0m | 100,000,000,000$ / c

Действие  : e
""",
    """Секунды   : 9,999,999,999,999 | Профиль : C
Минуты    : 282               | Уровень : 2,390
Часы      : 2                 | Доллары : 523,421,432,234$

11. Серый краситель

$ В секунду : 100,000$
Уровень     : 2

\033[32mУлучшение

$ В секунду : + 100,000$

Цена улучшения : 10,000 дерева
Дерево         : 123,921\033[0m

Действие  :""",
    """Статистика игрока Catalyst

Начало игры : 25.08.2020
Время игры  : 12 д 13 ч 21 мин 12 с 

Секунд получено : 5,839,860
Минут получено  : 97,411
Часов получено  : 1,622
Денег получено  : 234,329,513,123$

Максимальное время в афк : 10 д 1 ч 25 мин 30 с 
Прибыльное время в афк   : 2 ч 15 мин

Максимум денег в кошельке    : 10,234,289,532$
Денег в секунду за все время : 20,000 $ / с
Денег в секунду за красители : 40,000,000$ / с

Уровней куплено      : 613
Максимальный уровень : 250

Действие : 
""",
]


# отрисовка демок
# print(text[-3])
# for i in text: print(i)
def pn(number, recolor=0, mode=1):
    if not mode:
        number = int(number)
        return "{:,}".format(number) + " "

    else:
        number_backup = int(number)
        number = str(number)
        scale = ["", "k ", "m ", "b ", "q ", "Q "]
        scale_point = 0

        for i in range(15, 0, -3):
            if len(number) > i:
                number = str(int(number) / int("1" + "0" * i))
                number = number.rpartition(".")[0] + "." + number.rpartition(".")[2][:2]
                scale_point = int(i / 3)
                break

        if recolor:
            return number + scale[scale_point]
        else:
            return number + "\033[36m" + scale[scale_point] + "\033[0m"


def draw_res_count():
    money = 0

    res_stone = {
        "name": "Камень",
        "count": 0,
        "price": 1,
        "price_start": 1,
        "up_cost": 10,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_wood = {
        "name": "Дерево",
        "count": 0,
        "price": 5,
        "price_start": 5,
        "up_cost": 100,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_coal = {
        "name": "Уголь",
        "count": 0,
        "price": 50,
        "price_start": 50,
        "up_cost": 500,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_fabric = {
        "name": "Ткань",
        "count": 0,
        "price": 100,
        "price_start": 100,
        "up_cost": 1000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_copper = {
        "name": "Медь",
        "count": 0,
        "price": 200,
        "price_start": 200,
        "up_cost": 2000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_steel = {
        "name": "Железо",
        "count": 0,
        "price": 500,
        "price_start": 500,
        "up_cost": 4000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_gold = {
        "name": "Золото",
        "count": 0,
        "price": 1000,
        "price_start": 1000,
        "up_cost": 10000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_uranium = {
        "name": "Уран",
        "count": 0,
        "price": 2000,
        "price_start": 2000,
        "up_cost": 50000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_klit = {
        "name": "Кремнелит",
        "count": 0,
        "price": 5000,
        "price_start": 5000,
        "up_cost": 100000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    res_chromium = {
        "name": "Хром",
        "count": 0,
        "price": 10000,
        "price_start": 10000,
        "up_cost": 500000,
        "storage": 100,
        "per_s": 0.5,
        "level": 1,
    }

    # res_stone, res_wood, res_coal, res_fabric, res_copper, res_steel, res_gold, res_uranium, res_klit, res_chromium
    res_all = [
        res_stone,
        res_wood,
        res_coal,
        res_fabric,
        res_copper,
        res_steel,
        res_gold,
        res_uranium,
        res_klit,
        res_chromium,
    ]
    res_levels = [350, 300, 300, 300, 255, 255, 255, 255, 250, 235]

    for number in range(len(res_all)):
        i = res_all[number]
        for loop in range(res_levels[number] - 1):
            money -= i["up_cost"]
            i["level"] += 1
            # увеличение цены продажи
            i["price"] += i["price_start"]
            # бонус в 100 уровней
            if i["level"] % 100 == 0:
                i["price"] += i["price_start"]
                i["price_start"] *= 2
                i["price"] *= 2
                i["up_cost"] *= 1.4
            if i["level"] % 50 == 0:
                i["storage"] *= 2
            # увеличение стоимости улучшения
            i["up_cost"] *= 1.07
            # увеличение хранилища
            i["storage"] += i["level"] * 1.5
            # увеличение ресурсов в секунду
            i["per_s"] += 0.1

            print(
                i["name"],
                "\nУровень:",
                i["level"],
                "\nЦена улучшения:",
                pn(i["up_cost"]),
                "\nХранилище:",
                pn(i["storage"]),
                "\nВ секунду:",
                round(i["per_s"], 1),
                "\nДенег за все:",
                pn(abs(money)),
                "\n",
            )


# draw_res_count()
