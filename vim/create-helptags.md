# Create Helptags for new bundle

Some package managers, such as Vundle, will automatically generate help tags. Others, such as Pathogen, won't by default, so you have to do it yourself. Also, if you have installed Vdebug manually then you will also have to do this step.

For pathogen users, you can add this to your vimrc file to automatically generate helptags for your plugins:

    call pathogen#helptags()

To manually generate the tags, run this in vim:

    :helptags /path/to/vdebug/doc

where the path supplied is vdebug's doc directory. This should enable vdebug's help to be accessed.

Shamelessly lifted from https://github.com/joonty/vdebug

