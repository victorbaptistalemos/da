from bg_op import sys_clear
from bg_op import current_path
from json import dump as json_dump
from json import load as json_load


class TeamMember:
    def __init__(self, name: str, level: int, score: int, warning: int) -> None:
        self.__name = name
        self.__level = level
        self.__score = score
        self.__warning = warning

    def get_name(self) -> str:
        return self.__name

    def get_level(self) -> int:
        return self.__level

    def get_score(self) -> int:
        return self.__score

    def get_warning(self) -> int:
        return self.__warning

    def update_values(self, level: int, score: int, warning: int) -> None:
        self.__level = level
        self.__score = score
        self.__warning = warning


def add_member(arg: list[TeamMember]) -> list[TeamMember]:
    while True:
        try:
            list_member(arg)
            print()
            name: str = input('Informe o nome do(a) novo(a) participante: ')
            level: int = int(input('Informe o respectivo level: '))
            score: int = int(input('Informe o respectivo score: '))
            index: int = int(input('Informe em que posição deseja adicionar\n'
                                   f'"{len(arg) + 1}" para inserir no final da lista: '))
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


def list_member(arg: list[TeamMember]) -> None:
    print('Esta é a lista de participantes:')
    for _, member in enumerate(arg, start=1):
        print(f'{_}: {member.get_name()}')


def load_team() -> list[TeamMember]:
    team_json: dict
    with open(f'{current_path()}diggy.json', 'r') as diggy:
        team_json: dict = json_load(diggy)
    team_list: list = [TeamMember(key, *value) for key, value in team_json.items()]
    return team_list


def manage_member(arg: list[TeamMember]) -> list[TeamMember]:
    while True:
        try:
            if len(arg) < 30:
                member: str = input('Time incompleto. Deseja adicionar novo(a) participante [s/N]? ')
                if member.upper() == 'S':
                    arg: list[TeamMember] = add_member(arg)
                else:
                    raise UserWarning
                sys_clear()
            raise UserWarning
        except (EOFError, KeyboardInterrupt, UserWarning):
            break
    return arg


def manage_team(arg: list[TeamMember]) -> None:
    for _, member in enumerate(arg):
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
