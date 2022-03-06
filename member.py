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
            warning: int
    ) -> None:
        """
        When a team member data turns into an object.
        :param name: str
        :param level: int
        :param score: int
        :param warning: int
        """
        self.__name: str = name
        self.__level: int = level
        self.__score: int = score
        self.__warning: int = warning
        self.__is_warned: bool = self.__warned()
        self.__diff_score: int = 0

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
        check = lambda x: str(x).isdigit()
        if not all((check(level), check(score), check(warning))):
            return False
        else:
            self.__level = level
            self.__score = score
            self.__warning = warning
            return True

    @property
    def warnings(self) -> bool:
        """
        Acts like a getter method
        :return: bool
        """
        return self.__is_warned

    @property
    def difference(self) -> int:
        """
        Acts like a getter method
        :return: int
        """
        return self.__diff_score

    def __warned(self) -> bool:
        """
        Inner method. Checks if the Member object is warned.
        :return: bool
        """
        return self.__warning != 0
