import os
import shutil

disk_path = '/data/openpilot/selfdrive/controls/lib'
backup_path = '/data/openpilot-patch/backup'

for (parent, dirs, files) in os.walk(backup_path):
    for file in files:
        rel_path = f'{parent}/{file}'
        disk_full_path = f'{disk_path}/{rel_path}'
        if os.path.exists(disk_full_path):
            os.remove(disk_full_path)
        shutil.copy(f'{backup_path}/{rel_path}', disk_full_path)
        print(f'{rel_path} restored')
