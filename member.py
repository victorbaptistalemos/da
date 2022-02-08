"""
Module to operate on Team and TeamMember objects.
"""

from bg_op import current_path
from bg_op import sys_clear
from team import Team
from team import TeamMember


def adding_member(arg: Team) -> None:
    """
    Tries tp add a TeamMember on Team
    :param arg: Team
    :return: None
    """
    while True:
        try:
            list_member(arg)
            opt: list[TeamMember] = arg.get_team()
            print()
            name: str = input('Informe o nome do(a) novo(a) participante: ')
            level: int = int(input('Informe o respectivo level: '))
            score: int = int(input('Informe o respectivo score: '))
            index: int = int(input('Informe em que posição deseja adicionar\n'
                                   f'"{len(opt) + 1}" para inserir no final da lista: '))
            if index == 1:
                print(
                    f'Você está tentando adicionar: {name} antes de '
                    f'{opt[index -1].get_name()}.'
                )
            elif index == len(opt) + 1:
                print(
                    f'Você está tentando adicionar: {name} depois de '
                    f'{opt[index - 2].get_name()}.'
                )
            else:
                print(
                    f'Você está tentando adicionar: {name} entre '
                    f'{opt[index - 2].get_name()} e '
                    f'{opt[index - 1].get_name()}'
                )
            index -= 1
            input(f'Pressione Enter para confirmar ou Ctrl + C (^C) para voltar.')
            arg.add_member(TeamMember(name, level, score, 0), index)
            break
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
                break


def entering_member(arg: Team) -> None:
    """
    Verifies if the Team has 30 TeamMember on its attribute.
    :param arg: Team
    :return: none
    """
    while True:
        try:
            if len(opt := arg.get_team()) < 30:
                sys_clear()
                print(f'Time incompleto.\nO time tem {len(opt)}/30 participantes.')
                print('Pressione Ctrl + C (^C) para continuar o script')
                _: str = input('Deseja adicionar novo(a) participante [s/N]? ')
                if not _.isalnum() or _.upper() == 'S':
                    if adding_member(arg):
                        raise UserWarning
                    else:
                        print('Ocorreu algum erro, tente novamente!')
                else:
                    raise UserWarning
            else:
                raise UserWarning
        except (EOFError, KeyboardInterrupt, UserWarning):
            break


def list_member(arg: Team) -> None:
    """
    Prints the current TeamMember name list
    :param arg: Team
    :return: none
    """
    sys_clear()
    print('Esta é a lista de participantes:')
    for _, member in enumerate(arg.get_team(), start=1):
        print(f'{_}: {member.get_name()}')


def load_team() -> Team:
    """
    Grabs the info from a JSON file and turns it into a Team object.
    :return: Team
    """
    from json import load
    team: dict = {}
    sys_clear()
    try:
        with open(f'{current_path()}diggy.json', 'r') as diggy:
            team: dict = load(diggy)
    except FileNotFoundError:
        pass  # There's nothing to do. Will create a team from scratch.
    team: list[TeamMember] = [TeamMember(key, *value) for key, value in team.items()]
    team: Team = Team(team)
    return team


def manage_team(arg: Team) -> None:
    """
    Iterates on each TeamMember object and update its values.
    :param arg: Team
    :return: None
    """
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
                            print(f'Valor de {info} não compatível com o armazenado em {data} = {value}\n')
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
                arg.set_member(_, *new_player_data)
                sys_clear()
                break
            except (EOFError, KeyboardInterrupt):
                sys_clear()
                continue


def quitting_member(arg: Team) -> None:
    """
    Removes a TeamMember from Team.
    :param arg: Team
    :return: None
    """
    while True:
        try:
            sys_clear()
            print('Há alguém do grupo que saiu? ')
            input('Pressione Enter para confirmar ou Ctrl + c (^C) para continuar o script. ')
            list_member(arg)
            opt: int = int(input('Digite o índice que deseja excluir: ')) - 1
            print(f'{arg.get_team()[opt].get_name()} realmente saiu do grupo? ')
            input('Pressione Enter para confirmar ou Ctrl + C (^C) para cancelar.')
            arg.remove_member(arg.get_team()[opt])
        except (EOFError, IndexError, KeyboardInterrupt, ValueError):
            break


def remove_member(arg: Team) -> None:
    """
    TeamMember which matches a specific condition will be removed from Team.
    :param arg: Team
    :return: None
    """
    members_name: list = [member.get_name() for member in arg.get_team()]
    warned_member: list = [member.get_name() for member in arg.get_team() if member.get_warning() >= 10]
    for member in warned_member:
        removing = input(f'Deletar {member} do grupo? ')
        if not removing.isalnum() or removing.upper() == 'S':
            index: int = members_name.index(member)
            members_name.pop(index)
            arg.remove_member(arg.get_team()[index])
        else:
            continue


def write_team(arg: Team) -> None:
    """
    Writes the updated Team into a JSON file.
    :param arg: Team
    :return: None
    """
    from json import dump
    arg: list[TeamMember] = arg.get_team()
    arg: list[list] = [
        [
            member.get_name(),
            member.get_level(),
            member.get_score(),
            member.get_warning()
         ] for member in arg
    ]
    arg: dict[list] = {member[0]: [int(_) for _ in member[1:]] for member in arg}
    with open(f'{current_path()}diggy.json', 'w') as diggy:
        dump(arg, diggy, indent=True, ensure_ascii=False)
