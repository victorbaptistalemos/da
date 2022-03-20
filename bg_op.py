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
    cur_path: str = current_path()
    bkp_path: str = cur_path + f'diggy_{current_date()}.json'
    cur_path += 'diggy.json'
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
    arg: list = arg.split(' ')  # [date, time]
    arg.extend(
        arg.pop(0).split('-')  # date -> [d, m, y]
    )  # [date, time] -> [time, y, m, d]
    arg.extend(
        arg.pop(0).split(':')  # time -> [h, m, s]
    )  # [time, y, m, d] -> [y, m, d, h, m, s]
    arg[-1]: float = float(arg[-1])  # 'n.nnnnn' -> n.nnnnn
    arg[-1]: int = int(arg[-1])  # n.nnnnn -> n | nn
    arg[-1]: str = f'{arg[-1]:0=2d}'  # n | nn -> 'nn'
    arg: str = '_'.join(arg)  # [y, m, d, h, m, s] -> 'y_m_d_h_m_s'
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
    arg += command('path')
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
    cmd = command('clear')
    console(cmd)
