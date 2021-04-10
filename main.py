import random
p_win = 0
b_win = 0
patterns = {1: 'к', 2: 'н', 3: 'б', 4: 'выход'}

win_combination = [('к','н'),('н','б'),('б','к')]

while True:
    print('Вы играете в камень ножницы бумага. к - камень, н - ножницы, б - бумага.Чтобы выйти напишите: выход.')
    player = input('Ваш выбор:')
    if player not in patterns.values():
        print('Ход не выполнен!')
    elif player == 'выход':
        break
    comp_choice = patterns.get(random.randint(1, 3))
    print(f'Соперник выбрал: {comp_choice}')
   
    if player == comp_choice:
        print('Ничья')
    elif (player, comp_choice) in win_combination:
        p_win += 1
        print('Вы победили')
    else:
        b_win += 1
        print('Победа опонента')
        print(f'Статистика игры:\n Вы - {p_win}\n Компьютер - {b_win}')