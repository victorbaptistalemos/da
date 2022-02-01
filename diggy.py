#! /bin/python3

from bg_op import current_date
from bg_op import manage_backup
from bg_op import sys_clear
from team import load_team
from team import manage_member
from team import manage_team
from team import Member
from team import remove_member
from team import write_team


backup: None = None
try:
    sys_clear()
    team: list[Member] = load_team()
    backup: str = manage_backup(True, current_date())  # Creates a backup
    manage_member(team)
    manage_team(team)
    remove_member(team)
    write_team(team)
except (EOFError, KeyboardInterrupt):
    manage_backup(False, backup)  # Deletes the current backup
finally:
    sys_clear()
