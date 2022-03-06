#! /bin/python3
"""
Main module.
"""

from bg_op import manage_backup
from team import Team


backup: None = None
try:
    team: Team = Team()
    backup: str = manage_backup()  # Creates a backup
    team.manage_team()
    team.write_team()
except UserWarning:
    manage_backup(False, backup)  # Deletes the current backup
