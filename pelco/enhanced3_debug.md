# Turning on/off the Fan on enhanced3

run `/usr/sbin/pcp2sh` and do this:

```bash
> help(Switch_0027)
Switch_0027 help:
   -------
   METHODS
   	get_state
   	set_state
   -------
   ERRORS
   	switch_failure
> Switch_0027[1]:set_state(0,0)
switch_0027:state_change fired at peripheral address 0x0408
0
{error_id=0}
> Switch_0027[1]:set_state(0,1) 
switch_0027:state_change fired at peripheral address 0x0408
0
{error_id=0}
>     
```



