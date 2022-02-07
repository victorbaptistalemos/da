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


class Team:
    def __init__(self):
        self.__team: list[TeamMember] = []

    def get_team(self) -> list[TeamMember]:
        return self.__team

    def add_member(self, arg: TeamMember, index: int = -1) -> None:
        self.__team.insert(index, arg)

    def remove_member(self, arg: TeamMember) -> None:
        self.__team.remove(arg)
