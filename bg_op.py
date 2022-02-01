from datetime import datetime
from os import name as os_name
from os import system
from os.path import abspath
from os.path import dirname


def current_date() -> str:
    return str(datetime.now()).split(' ')[0]


def current_path() -> str:
    return abspath(dirname(__file__)) + ('\\' if os_name == 'nt' else '/')


def manage_backup(create_bkp: bool, bkp_name: str) -> [str, None]:
    if create_bkp:
        _path: str = current_path()
        bkp_name: str = _path + f'diggy_{bkp_name}.json'
        system(f"{'copy' if os_name == 'nt' else 'cp'} {_path}diggy.json {bkp_name}")
        return bkp_name
    else:
        system(f"{'remove' if os_name == 'nt' else 'rm'} {bkp_name}")


def sys_clear() -> None:
    system(f"{'cls' if os_name == 'nt' else 'clear'}")
