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


def console(arg1: str, arg2: str = '', arg3: str = '') -> None:
    """
    Receives a command to be executed from terminal.
    :param arg1: str
    :param arg2: str
    :param arg3: str
    :return: None
    """
    from os import system
    system(f'{arg1} {arg2} {arg3}')


def create_backup() -> str:
    """
    Creates a backup file.
    :return: str
    """
    cur_path: str = current_path() + 'diggy.json'
    bkp_path: str = cur_path + f'diggy_{current_date()}.json'
    cmd: str = command('cp')
    console(cmd, cur_path, bkp_path)
    return bkp_path


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


def delete_backup(arg: str) -> None:
    """
    Deletes a backup file.
    :param arg: str
    :return: None
    """
    cmd: str = command('rm')
    console(cmd, arg)
    sys_clear()


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
