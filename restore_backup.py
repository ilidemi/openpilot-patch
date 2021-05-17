import os
import shutil

disk_path = '/data/openpilot/selfdrive/controls/lib'
backup_path = '/data/openpilot-patch/backup'

for (parent, dirs, files) in os.walk(backup_path):
    for file in files:
        backup_full_path = f'{parent}/{file}'
        disk_full_path = backup_full_path.replace(backup_path, disk_path)
        if os.path.exists(disk_full_path):
            os.remove(disk_full_path)
        shutil.copy(backup_full_path, disk_full_path)
        print(f'{backup_full_path} restored')
