"""
Module to operate on Team and TeamMember objects.
"""

from bg_op import current_path
from bg_op import sys_clear
from member import Member


class Team:
    """
    All Member objects must be inside here.
    """
    def __init__(self):
        """
        Creates an empty list waiting for each TeamMember object to be inserted.
        """
        self.__team: list[Member] = []
        self.__load_team()

    def __add_member(self, arg: Member, index: int) -> bool:
        """
        Acts like a setter method.
        Adds a TeamMember object to the list.
        :param arg: Member,
        :param index: int
        :return: bool
        """
        if arg.__class__ is not Member:
            return False
        else:
            self.__team.insert(index, arg)
            return True

    def __adding_member(self) -> None:
        """
        Tries to add a Member into __team attribute.
        :return: None
        """
        while True:
            try:
                self.__list_member()
                print()
                opt: int = len(self.__team) + 1
                name: str = input('Name: ')
                level: int = int(input('Level: '))
                score: int = int(input('Score: '))
                index: int = int(input('Insert index number.\n'
                                       f'"{opt}" for end of list: '))
                if index == 1:
                    print(f'You\'re trying to add {name} before {self.__team[index - 1].get_name()}.')
                elif index == opt:
                    print(f'You\'re trying to add {name} after {self.__team[index - 2].get_name()}.')
                else:
                    after: str = self.__team[index - 2].get_name()
                    before: str = self.__team[index - 1].get_name()
                    print(f'You\'re trying to add {name} between {after} and {before}.')
                index -= 1
                input(f'Confirm pressing Enter or Cancel pressing Ctrl + C (^C).')
                if self.__add_member(Member(name, level, score, 0, True), index):
                    break
                else:
                    raise UserWarning
            except (EOFError, KeyboardInterrupt, ValueError):
                try:
                    sys_clear()
                    input('An error was raised.\nPress Enter to try again or Ctrl + C (^C) to skip.')
                    sys_clear()
                except (EOFError, KeyboardInterrupt):
                    break

    def __entering_member(self) -> None:
        """
        Tries to add a Member object into __team attribute.
        :return: none
        """
        while len(opt := self.__team) < 30:
            try:
                sys_clear()
                print(f'The team is incomplete!\nIt has {opt} of 30 members.')
                action: str = input('Press Ctrl + C (^C) to skip.\nDo you want to add a member? [Y/n]: ')
                if action.upper() == 'Y':
                    self.__adding_member()
                else:
                    break
            except (EOFError, KeyboardInterrupt):
                break

    def __list_member(self) -> None:
        """
        Prints the current Member status of __team attribute.
        :return: none
        """
        sys_clear()
        print('This is the current member list:')
        for m, member in enumerate(self.__team, start=1):
            print(f'\t{m}: {member.get_name()}')

    def __load_team(self) -> None:
        """
        Grabs the info from a JSON file and turns it into a Team object.
        :return: Team
        """
        from json import load
        self.__team: dict = {}
        sys_clear()
        try:
            with open(f'{current_path()}diggy.json', 'r') as diggy:
                self.__team: dict = load(diggy)
        except FileNotFoundError:
            pass  # There's nothing to do. Will create a Team from scratch.
        finally:
            self.__team: list[Member] = [Member(key, *value) for key, value in self.__team.items()]

    def manage_team(self) -> None:
        """
        Iterates on each Member object on __team attribute and update its values.
        :return: None
        """
        try:
            sys_clear()
            self.__quitting_member()  # Tries to remove a Member object.
            sys_clear()
            self.__entering_member()  # Tries to add a Member object.
            sys_clear()
            for m, member in enumerate(self.__team):
                while True:  # Will break after updating a Member object
                    member_name: str = member.get_name()
                    member_data: list[int] = [member.get_level(), member.get_score(), member.get_warning()]
                    new_data: list = []
                    opt = ('level', 'score')
                    for k, v in zip(opt, member_data):
                        info: None = None
                        while True:  # Will break after getting some info.
                            try:
                                print(f'Usuário: {member_name}, '
                                      f'Level: {member_data[0]}, '
                                      f'Score: {member_data[1]}, '
                                      f'Warnings: {member_data[2]}')
                                info: int = int(input(f'Digite o {k} atual de {member_name}: '))
                                if info < v or info >= v + 500:
                                    raise ValueError
                                else:
                                    new_data.append(info)
                                    sys_clear()
                                    break
                            except ValueError:
                                sys_clear()
                                if info is None:
                                    new_data.append(v)
                                    break
                                else:
                                    print(f'Valor de {info} não compatível com o armazenado em {k} = {v}\n')
                                    continue
                    try:
                        if new_data == member_data[:2]:
                            new_data.append(member_data[2] + 1)
                        else:
                            new_data.append(0)
                        print(
                            'Valores atuais de {}:\n'
                            '\tLevel: {}\n'
                            '\tScore: {}\n'.format(member_name, *member_data))
                        print(
                            'Novos valores de {}:\n'
                            '\tLevel: {}\n'
                            '\tScore: {}\n'.format(member_name, *new_data))
                        print('Pressione Enter para confirmar ou Ctrl + C (^C) para alterar.')
                        input()  # May raise an EOFError or a KeyboardInterrupt except
                        self.__set_member(m, * new_data)
                        sys_clear()
                        break
                    except (EOFError, KeyboardInterrupt):
                        sys_clear()
                        continue
            self.__remove_warned_member()
        except (EOFError, KeyboardInterrupt):
            raise UserWarning

    def __quitting_member(self) -> None:
        """
        Tries to remove a Member object from __team attribute.
        :return: None
        """
        while True:
            try:
                sys_clear()
                self.__list_member()
                print('\nHá alguém do grupo que saiu?')
                input('Pressione Enter para confirmar ou Ctrl + c (^C) para continuar o script. ')
                opt: int = int(input('Digite o índice que deseja excluir: ')) - 1
                print(f'{self.__team[opt].get_name()} realmente saiu do grupo? ')
                input('Pressione Enter para confirmar ou Ctrl + C (^C) para cancelar.')
                self.__remove_member(self.__team[opt])
            except (EOFError, IndexError, KeyboardInterrupt, ValueError):
                break

    def __remove_member(self, arg: Member) -> None:
        """
        Acts like a setter method.
        Removes a Member object from the __team attribute.
        :return: None
        """
        self.__team.remove(arg)

    def __set_member(self, index: int, level: int, score: int, warning: int) -> None:
        """
        Acts like a setter method.
        Updates a Member object from __team attribute.
        :return: None
        """
        self.__team[index].update_values(level, score, warning)

    def __remove_warned_member(self) -> None:
        """
        Tries to remove some Member from __team attribute which matches a specific condition.
        :return: None
        """
        members_name: list = [m.get_name() for m in self.__team]
        warned_member: list = [m.get_name() for m in self.__team if m.get_warning() >= 10]
        for wm in warned_member:
            sys_clear()
            removing = input(f'Deletar {wm} do grupo? ')
            if removing.upper() == 'S':
                index: int = members_name.index(wm)
                members_name.pop(index)
                self.__remove_member(self.__team[index])
            else:
                continue

    def write_team(self) -> None:
        """
        Writes the __team attribute into a JSON file.
        :return: None
        """
        from json import dump
        self.__team: list[list] = [
            [
                member.get_name(),
                member.get_level(),
                member.get_score(),
                member.get_warning()
             ] for member in self.__team
        ]
        self.__team: dict[list] = {member[0]: [int(_) for _ in member[1:]] for member in self.__team}
        with open(f'{current_path()}diggy.json', 'w') as diggy:
            dump(self.__team, diggy, indent=True, ensure_ascii=False)
        sys_clear()
