"""
Main module.
"""

from bg_op import create_backup
from bg_op import delete_backup
from team import Team


backup: None = None
try:
    team: Team = Team()  # Creates a Team object from a JSON file
    backup: str = create_backup()  # Creates a backup
    team.manage_team()  # Changes the Team object attribute
    team.write_team()  # Creates a JSON file from changes
except UserWarning:
    delete_backup(backup)  # Deletes the current backup
