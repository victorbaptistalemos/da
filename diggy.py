#! /bin/python3
"""
Main module.
"""

from bg_op import manage_backup
from member import load_team
from member import manage_team
from member import remove_member
from member import write_team
from team import Team


backup: None = None
try:
    team: Team = load_team()
    backup: str = manage_backup()  # Creates a backup
    manage_team(team)
    remove_member(team)
    write_team(team)
except (EOFError, KeyboardInterrupt):
    manage_backup(False, backup)  # Deletes the current backup
