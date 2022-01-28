#! /bin/python3

from bg_op import current_time, manage_backup, sys_clear
from team import load_team, manage_member, manage_team, Member, remove_member, write_team

backup: None = None
try:
    team: list[Member] = load_team()
    backup: str = manage_backup(True, current_time())  # Creates a backup
    manage_member(team)
    manage_team(team)
    remove_member(team)
    write_team(team)
except (EOFError, KeyboardInterrupt):
    manage_backup(False, backup)
finally:
    sys_clear()
