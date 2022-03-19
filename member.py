"""
Module to manage the team members.
"""


class Member:
    """
    Every member of team should be instantiated here.
    """
    def __init__(
            self,
            name: str,
            level: int,
            score: int,
            warning: int,
            is_new: bool = False
    ) -> None:
        """
        When a team member data turns into an object.
        :param name: str,
        :param level: int,
        :param score: int,
        :param warning: int,
        :param is_new: bool
        """
        self.__name: str = name
        self.__level: int = level
        self.__score: int = score
        self.__warning: int = warning
        self.__is_new: bool = is_new

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

    def update_values(self, level: int, score: int) -> None:
        """
        Acts like a setter method.
        Updates some attributes.
        :param level: int,
        :param score: int
        :return: None
        """
        warning: tuple = (level == self.__level, score == self.__score)
        warning: bool = all(warning)
        warning: bool = warning and not self.__is_new
        self.__level = level
        self.__score = score
        if warning:
            self.__warning += 1
