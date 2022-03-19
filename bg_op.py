"""
This module executes some background operations.
"""


def command(arg: str) -> str:
    """
    Returns a command name
    :param arg: str
    :return: str
    """
    cmd: dict = {
        'clear': {True: 'cls', False:  'clear'},
        'cp': {True: 'copy', False:  'cp'},
        'path': {True: '\\', False:  '/'},
        'rm': {True: 'remove', False:  'rm'},
    }
    return cmd[arg][is_win()]


def console(arg) -> None:
    """
    Receives a command to be executed from terminal.
    :param arg: str
    :return: None
    """
    from os import system
    system(arg)


def current_date() -> str:
    """
    Catches the current date.
    :return: str
    """
    from datetime import datetime
    arg: datetime = datetime.now()
    arg: str = str(arg)
    arg: list = arg.split(' ')
    arg: str = arg[0]
    return arg


def current_path() -> str:
    """
    Catches the absolute path.
    :return: str
    """
    from os.path import abspath
    from os.path import dirname
    arg: str = __file__
    arg: str = dirname(arg)
    arg: str = abspath(arg)
    arg += '\\' if is_win() else '/'
    return arg


def is_win() -> bool:
    """
    Is this script running on a Windows OS?
    :return: bool
    """
    from os import name
    return name == 'nt'


def sys_clear() -> None:
    """
    Clears the terminal.
    :return: None
    """
    arg: str = 'cls' if is_win() else 'clear'
    console(arg)
