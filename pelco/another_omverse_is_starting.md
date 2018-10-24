# Fixing the "Another omverse is starting" error

Use bash to find and kill the running omverse processes:
```bash
$ ps -ef | grep omv
root      7801  7798  0 14:06 pts/1    00:00:00 sudo /opt/omtools/bin/omverse -b /mnt/wormhole/home/jima/work/omons/external-3rdparty/libcap/2.20 /mnt/wormhole/home/jima/work/omons/build-tools/sebu_build.py
root      7806  7801  0 14:06 pts/1    00:00:00 /bin/bash /opt/omtools/bin/omverse -b /mnt/wormhole/home/jima/work/omons/external-3rdparty/libcap/2.20 /mnt/wormhole/home/jima/work/omons/build-tools/sebu_build.py
jima      7820  5045  0 14:06 pts/0    00:00:00 grep omv

$ sudo kill -9 7801 7806
$ ps -ef | grep omv
```

Once all the omverse processes have been killed, remove the lock files:

```bash
$ cd /var/run/
$ sudo rm omverse.*
```
