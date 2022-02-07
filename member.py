"""
Module to operate on Team and TeamMember objects.
"""
# First I'll write the functions by diggy.py module calling.


from bg_op import current_path
from bg_op import sys_clear
from team import Team
from team import TeamMember


# 1st call
def load_team() -> Team:
    from json import load
    team: dict
    sys_clear()
    try:
        with open(f'{current_path()}diggy.json', 'r') as diggy:
            team: dict = load(diggy)
    except FileNotFoundError:
        pass  # There's nothing to do. Will create a team from scratch.
    team: list[TeamMember] = [TeamMember(key, *value) for key, value in team.items()]
    team: Team = Team(team)
    return team


# 2nd call
def manage_team(arg: Team) -> None:
    sys_clear()
    quitting_member(arg)  # If someone leaves the team, here's the function to remove him.
    sys_clear()
    entering_member(arg)  # If the team is not full it'll attempt to add someone.
    sys_clear()
    for _, member in enumerate(arg.get_team()):
        while True:
            player_name: str = member.get_name()
            player_data: list[int] = [member.get_level(), member.get_score(), member.get_warning()]
            new_player_data: list = []
            for data, value in zip(('level', 'score'), player_data):  # will cut the last element of player_data
                info: None = None
                while True:
                    try:
                        print(f'Usuário: {player_name}, '
                              f'Level: {player_data[0]}, '
                              f'Score: {player_data[1]}, '
                              f'Warnings: {player_data[2]}')
                        info: int = int(input(f'Digite o {data} atual de {player_name}: '))
                        if info < value or info >= value + 500:
                            raise ValueError
                        else:
                            new_player_data.append(info)
                            sys_clear()
                            break
                    except ValueError:
                        sys_clear()
                        if info is None:
                            new_player_data.append(value)
                            break
                        else:
                            print(f'Valor de {info} não compatível com o armazenado em {data} = {value}')
                            continue
            try:
                print('Valores atuais de {}: Level: {}, Score: {}'.format(player_name, *player_data))
                print('Novos valores de {}: Level: {}, Score: {}'.format(player_name, *new_player_data))
                print('\nPressione Enter para confirmar ou Ctrl + C (^C) para alterar.')
                input()
                if new_player_data == player_data[:2]:
                    new_player_data.append(player_data[2] + 1)
                else:
                    new_player_data.append(0)
                arg[_].update_values(*new_player_data)
                sys_clear()
                break
            except (EOFError, KeyboardInterrupt):
                sys_clear()
                continue


# 3rd call from 2nd
def quitting_member(arg: Team) -> None:
    while True:
        try:
            sys_clear()
            print('Há alguém do grupo que saiu? ')
            input('Pressione Enter para confirmar ou Ctrl + c (^C) para continuar o script. ')
            list_member(arg)
        except (EOFError, KeyboardInterrupt):
            break


# 4th call from 3rd
def list_member(arg: Team) -> None:
    sys_clear()
    print('Esta é a lista de participantes:')
    for _, member in enumerate(arg.get_team(), start=1):
        print(f'{_}: {member.get_name()}')


# 5th call from 2nd
def entering_member(arg: Team) -> None:
    while True:
        try:
            if len(opt := arg.get_team()) < 30:
                sys_clear()
                print(f'Time incompleto.\nO time tem {len(opt)}/30 participantes.')
                print('Pressione Ctrl + C (^C) para continuar o script')
                _: str = input('Deseja adicionar novo(a) participante [s/N]? ')
                if not _.isalnum() or _.upper() == 'S':
                    adding_member(arg)
                else:
                    raise UserWarning
            else:
                raise UserWarning
        except (EOFError, KeyboardInterrupt, UserWarning):
            break


# 6th call from 5th
def adding_member(arg: Team) -> None:
    while True:
        try:
            list_member(arg)
            opt: int = len(arg.get_team())
            print()
            name: str = input('Informe o nome do(a) novo(a) participante: ')
            level: int = int(input('Informe o respectivo level: '))
            score: int = int(input('Informe o respectivo score: '))
            index: int = int(input('Informe em que posição deseja adicionar\n'
                                   f'"{opt + 1}" para inserir no final da lista: '))
            if index == 1:
                print(
                    f'Você está tentando adicionar: {name} antes de '
                    f'{arg[index -1].get_name()}.'
                )
            elif index == len(arg) + 1:
                print(
                    f'Você está tentando adicionar: {name} depois de '
                    f'{arg[index - 1].get_name()}.'
                )
            else:
                print(
                    f'Você está tentando adicionar: {name} entre '
                    f'{arg[index - 2].get_name()} e '
                    f'{arg[index - 1].get_name()}'
                )
            index -= 1
            input(f'Pressione Enter para confirmar ou Ctrl + C (^C) para voltar.')
            arg.insert(index, TeamMember(name, level, score, 0))
            return arg
        except (EOFError, KeyboardInterrupt, ValueError):
            try:
                sys_clear()
                input(
                    'Ocorreu um erro ao processar os dados\n'
                    'Pressione Enter para tentar novamente ou\n'
                    'Pressione Ctrl + C (^C) para atualizar os membros do grupo.'
                )
                sys_clear()
            except (EOFError, KeyboardInterrupt):
                return arg




























def remove_member(arg: list[TeamMember]) -> None:
    members_name: list = [member.get_name() for member in arg]
    warned_member: list = [member.get_name() for member in arg if member.get_warning() >= 7]
    for member in warned_member:
        delete = input(f'Deletar {member} do grupo? ')
        if delete.upper() == 'S':
            index: int = members_name.index(member)
            members_name.pop(index)
            arg.pop(index)
        else:
            continue


def write_team(arg: list[TeamMember]) -> None:
    arg: list[list] = [member.__repr__().split() for member in arg]
    arg: dict[list] = {member[0]: [int(_) for _ in member[1:]] for member in arg}
    with open(f'{current_path()}diggy.json', 'w') as diggy:
        json_dump(arg, diggy, indent=True)
