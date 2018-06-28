# Finding Files By Date and Deleting Them

Use the find command to find files older than a number of days with:

    find . -atime +68 -ls

Add the exec option to remove full directories:

    sudo find . -atime +60 -exec rm -rf {} \;

