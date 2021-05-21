from dataclasses import dataclass
from datetime import datetime
import hashlib
import os
import shutil
import subprocess
from sys import stdout

def log(message):
    print(f"{datetime.now()} {message}")
    stdout.flush()

log('Start')
disk_path = '/data/openpilot/selfdrive/controls/lib'
backup_path = '/data/openpilot-patch/backup'
target_path = '/data/openpilot-patch/src'

@dataclass
class HashedFile:
    rel_path: str
    orig_md5: str

hashed_files = [
    HashedFile('long_mpc.py', 'cd3cc9503927eff6b350f47dec90dc39'),
    HashedFile('longitudinal_planner.py', 'b4cf0480a5c54c7c7c3f58af7e361b0f'),
    HashedFile('longitudinal_mpc/longitudinal_mpc.c', '3e509bd185e5fee736b7aed568536c33'),
    HashedFile('longitudinal_mpc/lib_mpc_export/acado_solver.c', '6e731dad215753195cc960a555d7320a'),
    HashedFile('longitudinal_mpc/libmpc_py.py', '40563a2710e5824c3ede434f05b2d924'),
    HashedFile('longitudinal_mpc/libmpc1.so', 'fbf3a9c58f3ce9d14fb7818550577003'),
    HashedFile('longitudinal_mpc/libmpc2.so', 'fbf3a9c58f3ce9d14fb7818550577003')
]

new_files = [
    'dynamic_follow/__init__.py',
    'dynamic_follow/support.py'
]

def file_md5(path):
    with open(path, 'rb') as f:
        contents = f.read()
        return hashlib.md5(contents).hexdigest()

os.makedirs(backup_path, exist_ok=True)

files_to_backup = []
files_to_copy = new_files
for hashed_file in hashed_files:
    disk_md5 = file_md5(f'{disk_path}/{hashed_file.rel_path}')
    target_md5 = file_md5(f'{target_path}/{hashed_file.rel_path}')
    if disk_md5 == hashed_file.orig_md5:
        log(f'{hashed_file.rel_path} needs to be replaced')
        files_to_backup.append(hashed_file.rel_path)
        files_to_copy.append(hashed_file.rel_path)
    elif disk_md5 == target_md5:
        log(f'{hashed_file.rel_path} is same as target')
    else:
        log(f'{hashed_file.rel_path} has unknown hash: {disk_md5}')
        subprocess.Popen(['python', '/data/openpilot-patch/util/error.py'])
        raise Exception('Unknown hash')

for file_to_backup in files_to_backup:
    backup_full_path = f'{backup_path}/{file_to_backup}'
    if os.path.exists(backup_full_path):
        os.remove(backup_full_path)
    os.makedirs(os.path.dirname(backup_full_path), exist_ok=True)
        
    shutil.copy(f'{disk_path}/{file_to_backup}', backup_full_path)
    log(f'{file_to_backup} backed up')

for file_to_copy in files_to_copy:
    copy_full_path = f'{disk_path}/{file_to_copy}'
    if os.path.exists(copy_full_path):
        os.remove(copy_full_path)
    os.makedirs(os.path.dirname(copy_full_path), exist_ok=True)
    shutil.copy(f'{target_path}/{file_to_copy}', copy_full_path)
    log(f'{file_to_copy} copied')

log('Finish')
