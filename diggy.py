#! /bin/python

from json import dump, load
from os import system

try:
    system('clear')
    with open("diggy.json") as _:
        team: dict = load(_)  # {key: list, key: list, ...}
        new_team: dict = {}
    for key in team.keys():  # iterates on each player
        while True:
            player: list = team[key]  # [level, score, warning]
            new_data: list = []
            for name, value in zip(('level', 'score'), player):  # will cut the last element of player
                data: None = None
                while True:
                    try:
                        print(f'Usuário: {key}, Level: {player[0]}, Score: {player[1]}, Warnings: {player[2]}')
                        data: int = int(input(f'Digite o {name} atual de {key}: '))
                        if value > data or data >= value + 500:
                            raise ValueError
                        else:
                            new_data.append(data)
                            system('clear')
                            break
                    except ValueError:
                        system('clear')
                        if data is None:
                            new_data.append(value)
                            break
                        else:
                            print(f'Valor de {data} não compatível com o armazenado em {name} = {value}')
                            continue
            try:
                print('Valores atuais de {}: Level: {}, Score: {}'.format(key, *player))
                print('Novos valores de {}: Level: {}, Score: {}'.format(key, *new_data))
                print('\nPressione Enter para confirmar ou Ctrl + C (^C) para alterar.')
                input()
                if new_data == player[:2]:
                    new_data.append(player[2] + 1)
                else:
                    new_data.append(0)
                new_team[key] = new_data
                system('clear')
                break
            except KeyboardInterrupt:
                system('clear')
                continue
    del team, key, player, name, value, data, new_data
    w7 = [key for key in new_team.keys() if new_team[key][2] >= 7]
    for w in w7:
        delete = input(f'Deletar {w} do time? ')
        if len(delete) == 0 or delete in 'sS':
            del new_team[w]
        else:
            continue
    with open("diggy.json", 'w') as _:
        dump(new_team, _, indent=4)
except (EOFError, KeyboardInterrupt):
    pass
finally:
    system('clear')
