from datetime import datetime
from os import name as os_name
from os import system


def current_time() -> str:
    _time: datetime = datetime.now()
    _time: str = str(_time)
    _time: str = _time.split(' ')[0]
    return _time


def sys_clear() -> None:
    system(f"{'cls' if os_name == 'nt' else 'clear'}")


def manage_backup(create_bkp: bool, bkp_name: str) -> [str, None]:
    if create_bkp:
        bkp_name: str = f'diggy_{bkp_name}.json'
        system(f"{'copy' if os_name == 'nt' else 'cp'} diggy.json {bkp_name}")
        return bkp_name
    else:
        system(f"{'remove' if os_name == 'nt' else 'rm'} {bkp_name}")
