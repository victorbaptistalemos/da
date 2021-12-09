#! /bin/python

from json import dump, load
from os import system

try:
    system('clear')
    with open("diggy.json") as _:
        team: dict = load(_)
    for key in team.keys():
        l, s, w = team[key]
        level, score = None, None
        print(f'Usuário: {key}, Level: {l}, Score: {s}, Warnings: {w}')
        try:
            level: int = int(input(f'Digite o level atual de {key}: '))
        except ValueError:
            level: int = l
        try:
            score: int = int(input(f'Digite o score atual de {key}: '))
        except ValueError:
            score: int = s
        if (level, score) == (l, s):
            team[key][2] += 1
        else:
            team[key] = [level, score, 0]
        system('clear')
    w7 = [key for key in team.keys() if team[key][2] >= 7]
    for w in w7:
        delete = input(f'Deletar {w} do time? ')
        if len(delete) == 0 or delete in 'sS':
            del team[w]
        else:
            continue
    with open("diggy.json", 'w') as _:
        dump(team, _, indent=4)
except (EOFError, KeyboardInterrupt):
    pass
finally:
    system('clear')

