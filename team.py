"""
Module to manage the team members.
"""


class TeamMember:
    """
    Every member of team should be instantiated here.
    """
    def __init__(self, name: str, level: int, score: int, warning: int) -> None:
        """
        When a team member data turns into an object.
        :param name: str
        :param level: int
        :param score: int
        :param warning: int
        """
        self.__name = name
        self.__level = level
        self.__score = score
        self.__warning = warning

    def get_name(self) -> str:
        """
        This is a getter method!
        :return: str
        """
        return self.__name

    def get_level(self) -> int:
        """
        This is a getter method!
        :return: int
        """
        return self.__level

    def get_score(self) -> int:
        """
        This is a getter method!
        :return: int
        """
        return self.__score

    def get_warning(self) -> int:
        """
        This is a getter method!
        :return: int
        """
        return self.__warning

    def update_values(self, level: int, score: int, warning: int) -> bool:
        """
        Acts like a setter method.
        Updates some attributes.
        :param level: int
        :param score: int
        :param warning: int
        :return: None
        """
        try:
            if level is not int or score is not int or warning is not int:
                raise UserWarning
            else:
                self.__level = level
                self.__score = score
                self.__warning = warning
                return True
        except UserWarning:
            return False


class Team:
    """
    All team members should be inside here.
    """
    def __init__(self, team: [list[TeamMember], None] = None):
        """
        Creates an empty list waiting for each TeamMember object to be inserted.
        """
        self.__team: list[TeamMember]
        if list is None:
            self.__team = []
        else:
            self.__team = team

    def get_team(self) -> list[TeamMember]:
        """
        This is a getter method!
        :return: list
        """
        return self.__team

    def add_member(self, arg: TeamMember, index: [int, None] = None) -> bool:
        """
        Acts like a setter method.
        Adds a TeamMember object to the list.
        :return: bool
        """
        try:
            if arg.__class__ is not TeamMember:
                raise UserWarning
            elif index is None:
                self.__team.append(arg)
                return True
            else:
                self.__team.insert(index, arg)
                return True
        except (TypeError, UserWarning):
            return False

    def remove_member(self, arg: TeamMember) -> bool:
        """
        Acts like a setter method.
        Removes a TeamMember object from the list.
        :return: None
        """
        try:
            self.__team.remove(arg)
            return True
        except ValueError:
            return False

    def set_member(self, index: int, level: int, score: int, warning: int) -> bool:
        """
        Acts like a setter method.
        Updates a TeamMember object from the list.
        :return: None
        """
        try:
            if level is not int or score is not int or warning is not int:
                raise UserWarning
            else:
                self.__team[index].update_values(level, score, warning)
                return True
        except (IndexError, UserWarning):
            return False
