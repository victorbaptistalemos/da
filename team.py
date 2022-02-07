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

    def update_values(self, level: int, score: int, warning: int) -> None:
        """
        Acts like a setter method.
        Updates some attributes.
        :param level: int
        :param score: int
        :param warning: int
        :return: None
        """
        self.__level = level
        self.__score = score
        self.__warning = warning


class Team:
    """
    All team members should be inside here.
    """
    def __init__(self):
        """
        Creates an empty list waiting for each TeamMember object to be inserted.
        """
        self.__team: list[TeamMember] = []

    def get_team(self) -> list[TeamMember]:
        """
        This is a getter method!
        :return: list
        """
        return self.__team

    def add_member(self, arg: TeamMember, index: int = -1) -> None:
        """
        Acts like a setter method.
        Adds a TeamMember object to the list.
        :return: None
        """
        self.__team.insert(index, arg)

    def remove_member(self, arg: TeamMember) -> None:
        """
        Acts like a setter method.
        Removes a TeamMember object from the list.
        :return: None
        """
        self.__team.remove(arg)
