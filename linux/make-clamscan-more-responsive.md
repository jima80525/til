# Make clamscan or other high-cpu-load process play nice

If it's already running use:
    renice -n 19 <pid>

You can start it with the nice command, e.g.

    nice -n 19 clamscan

This does NOT limit the CPU, but it does lower the priority of the process.
