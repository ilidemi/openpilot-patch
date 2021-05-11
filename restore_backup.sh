set -e

disk_mpc_path=/data/openpilot/selfdrive/controls/lib/long_mpc.py
backup_mpc_path=/data/openpilot-patch/long_mpc_backup.py

rm -f $disk_mpc_path
mv $backup_mpc_path $disk_mpc_path
