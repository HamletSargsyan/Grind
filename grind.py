import time
import os
from threading import Thread

name = 'Catalyst'
game_exit = 0
money = 0
level = 0
move = ['']

help_text = '''Команды

Команда     - Действие
help        - список действий
enter       - обновить экран
exit        - сохранить игру и выйти
save        - сохранить игру
stats       - статистика
[name]      - показать данные ресурса
sell [name] - продать ресурс
open        - открыть ресурс
up [name]   - улучшение
'''

res_time = {'seconds': 0,
            'minutes': 0,
            'hours': 0,
            'wait_minutes': 0,
            'wait_hours': 0}

res_stone = {'name': 'Камень',
             'count': 0,
             'price': 1,
             'price_start': 1,
             'up_cost': 10,
             'storage': 100,
             'per_s': 0.5,
             'level': 1}

res_wood = {'name': 'Дерево',
             'count': 0,
             'price': 5,
             'price_start': 5,
             'up_cost': 100,
             'storage': 100,
             'per_s': 0.5,
             'level': 1}

res_coal = {'name': 'Уголь',
             'count': 0,
             'price': 50,
             'price_start': 50,
             'up_cost': 500,
             'storage': 100,
             'per_s': 0.5,
             'level': 1}

index = {'Камень': 0,
         'Дерево': 1,
         'Уголь': 2}

buy = [2, 0, 'Камень    : 1 минута; 10 секунд', 'Дерево    : 10 минут; 50 камней', 'Уголь     : 1 час; 100 дерева']
res_all = []

res_time['seconds'] += 1000
res_time['minutes'] += 20
res_time['hours'] += 10
res_stone['count'] += 100

# extension
def pn(number):
    number = round(number)
    if number >= 1000:
        iteration = 3
        iter_dash = 0
        out = str(number)
        while iteration < len(str(number)):
            out = out[:-iteration-iter_dash] + ',' + out[-iteration-iter_dash:]
            iteration += 3
            iter_dash += 1
        return out
    else: return str(number)

def gap(name):
    return (' ' * (15 - len(pn(name))))

def draw_storage(count, max_count):
    percents = round(count / max_count * 100)
    out = '['
    iteration = 0
    for i in range(0, percents // 10):
        iteration += 1
        out += '#'

    while iteration < 10:
        out += '.'
        iteration += 1

    return out+'] ' + str(percents) + '%' + ' ' * (3 - len(str(percents)))

def upgradable(up_cost):
    if money >= up_cost:
        return '|\033[32mo\033[0m|'
    else: return '|\033[31mx\033[0m|'

def draw_name(name):
    return name + ' ' * (10 - len(name)) + ':'

def sell(move):
    global money
    res_id = -1
    if move == 'all':
        for i in res_all:
            money += i['count'] * i['price']
            i['count'] = 0
    else:
        for i in index:
            if move == i:
                res_id = index[i]
                break
    
        for i in index:
            i = index[i]
            if move == str(i + 1):
                res_id = int(i)
                break

        if len(res_all) > res_id and res_id != -1:
            money += res_all[res_id]['count'] * res_all[res_id]['price']
            res_all[res_id]['count'] = 0

# functions
def draw_header():
    os.system('clear')
    print('Секунды   :', pn(res_time['seconds']), gap(res_time['seconds']) + '| Профиль :', name)
    print('Минуты    :', pn(res_time['minutes']), gap(res_time['minutes']) + '| Уровень :', pn(level))
    print('Часы      :', pn(res_time['hours']), gap(res_time['hours']) + '| Деньги  :', pn(money) + '$')

def draw_buy():
    if buy[0] <= 3 + 1:
        buy[1] = 0
        if buy[0] == 2:
            if res_time['seconds'] >= 10 and res_time['minutes'] >= 1:
                buy[1] = 1
        if buy[0] == 3:
            if res_time['minutes'] >= 10 and res_all[0]['count'] >= 50:
                buy[1] = 1
        if buy[0] == 4:
            if res_time['hours'] >= 1 and res_all[1]['count'] >= 100:
                buy[1] = 1
        if buy[1] == 1: print('\n' + buy[buy[0]])

def draw_res():
    if res_all:
        print('')
        for i in res_all:
            print(draw_name(i['name']), pn(i['count']), gap(i['count']) + '|', draw_storage(i['count'], i['storage']), upgradable(i['up_cost']), pn(i['price'] * i['count']) + '$')

# game loops
def progress():
    global res_time
    while 1:
        time.sleep(1)
        res_time['wait_minutes'] += 1     
        res_time['wait_hours'] += 1    
        res_time['seconds'] += 1

        if res_time['wait_minutes'] == 60:
            res_time['wait_minutes'] = 0
            res_time['minutes'] += 1  

        if res_time['wait_hours'] == 3600:
            res_time['wait_hours'] = 0  
            res_time['hours'] += 1  

        if res_all:
            for i in res_all:
                i['count'] += i['per_s']
                if i['count'] > i['storage']:
                    i['count'] = i['storage']
                i['count'] = round(i['count'], 1)

        if game_exit == 1:
            os._exit(1)

def game_render():
    while 1:
        global money, move

        draw_header()
        draw_res()
        draw_buy()

        if move == ['']:
            move = input('\nДействие  : ').split(' ')
        else:
            print('\nДействие  :', move[0])

        if move[0] == 'quit' or move[0] == 'exit' or move[0] == 'e':
            game_exit = 1
            os.system('clear')
            os._exit(1)
            move = ['']
        
        elif move[0] == 'help':
            os.system('clear')
            print(help_text)
            move = input('\nДействие  : ').split(' ')
        
        elif move[0] == 'open' and buy[1] == 1:
            if buy[0] == 2:
                res_time['seconds'] -= 10
                res_time['minutes'] -= 1
                res_all.append(res_stone)

            if buy[0] == 3:
                res_time['minutes'] -= 10
                res_all[0]['count'] -= 50
                res_all.append(res_wood)

            if buy[0] == 4:
                res_time['hours'] -= 1
                res_all[1]['count'] -= 100
                res_all.append(res_coal)

            buy[1] == 0
            buy[0] += 1
            move = ['']
        
        elif move[0] == 'sell' and move[-1] != 'sell':
            sell(move[1])
            move = ['']

        elif move[0] == 'up':
            i = 0
            loop = 1
            try: 
                res_id = index[move[1]]
                i = res_all[res_id]
                
            except Exception:
                try:
                    i = res_all[int(move[1]) - 1]
                except Exception: pass
            try:
                if move[2] == 'max': loop = 'max'
                else: loop = int(move[2])
            except Exception: pass
            if i:
                while 1:
                    if money >= i['up_cost']:
                        money -= i['up_cost']
                        # увеличение цены продажи
                        i['level'] += 1
                        i['price'] +=  i['price_start']
                        if i['level'] % 100 == 0:
                            i['price_start'] *= 2
                            i['price'] *= 2
                            i['up_cost'] *= 1.4
                        # увеличение стоимости улучшени]
                        i['up_cost'] *= 1.07
                        # увеличение хранилища
                        i['storage'] = i['price'] * i['level'] * 2
                        # увеличение ресурсов в секунду
                        i['per_s'] += 0.1
                        if loop != 'max': 
                            loop -=1
                            if loop <= 0: break
                    else: break
            move = ['']

        elif move != ['']: # res stats
            i = 0
            try: 
                res_id = index[move[0]]
                i = res_all[res_id]
                os.system('clear')
                print(str(res_id+1)+'.', move[0] + '\n')
            except Exception:
                try:
                    i = res_all[int(move[0]) - 1]
                    os.system('clear')
                    print(move[0]+'.', i['name'] + '\n')
                except Exception: pass
            if i:
                print('Колличество :', pn(i['count']), '\nХранилище   :', i['storage'],'\nСтоимость 1 :', pn(i['price']) + '$', '\nВ секунду   :', pn(i['per_s']), '\nУровень     :', pn(i['level']), '\n\nУлучшение\n')
                if money >= i['up_cost']: print('\033[32m', end='')
                else: print('\033[31m', end='')
                if i['level'] % 100 == 0: print('Стоимость 1 :', '+' + str(i['price'] + i['price_start']))
                else: print('Стоимость 1 :', '+' + str(i['price_start']))
                print('В секунду   :', '+0.1')
                print('Хранилище   :', '+' + pn(i['price']*i['level']*2))
                print('\nЦена улучшения :', pn(i['up_cost']) + '$')
                print('\033[0m', end='')

                move = input('\nДействие  : ').split(' ')
            else: move = ['']

            

time_l = Thread(target=progress)
render_l = Thread(target=game_render)

time_l.start()
render_l.start()

time_l.join()
render_l.join()
