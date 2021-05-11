set -e

setenforce 0
rm -f /data/local/userinit.sh
cp userinit.sh /data/local/userinit.sh
