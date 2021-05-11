set -e

log_path=/data/openpilot/log.txt

echo $(date -u) "Start" >> $log_path

disk_mpc_path=/data/openpilot/selfdrive/controls/lib/long_mpc.py
target_mpc_path=/data/openpilot-patch/long_mpc.py
backup_mpc_path=/data/openpilot-patch/long_mpc_backup.py

disk_md5=md5sum $disk_mpc_path | awk '{ print $1 }'
target_md5=md5sum $target_mpc_path | awk '{ print $1 }'
orig_md5=cd3cc9503927eff6b350f47dec90dc39

if [[ $disk_md5 == $orig_md5 ]]; then
    echo $(date -u) "Replacing disk with target" >> $log_path
    mv $disk_mpc_path $backup_mpc_path
    cp $target_mpc_path $disk_mpc_path
else
    if [[ $disk_md5 == $target_md5 ]]; then
        echo $(date -u) "Disk is same as target" >> $log_path
    else
        echo $(date -u) "Unknown disk hash:" $disk_md5 >> $log_path
        python /data/openpilot-patch/error.py
    fi
fi

echo $(date -u) "Finish" >> $log_path
