# Enabling core files on Centos

To enable core file generation in general use `ulimit -S -c unlimited`.  To turn 
it back off, use `ulimit -S -c 0`.
