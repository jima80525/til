# Stash Only Some of the Changed Files

Use the `-p` flag to put `git stash save` into patch mode:

```bash
git stash save -p "name of stash"
```

You'll be prompted with a few actions for each hunk:

```text
   y - stash this hunk
   n - do not stash this hunk
   q - quit; do not stash this hunk or any of the remaining ones
   a - stash this hunk and all later hunks in the file
   d - do not stash this hunk or any of the later hunks in the file
   g - select a hunk to go to
   / - search for a hunk matching the given regex
   j - leave this hunk undecided, see next undecided hunk
   J - leave this hunk undecided, see next hunk
   k - leave this hunk undecided, see previous undecided hunk
   K - leave this hunk undecided, see previous hunk
   s - split the current hunk into smaller hunks
   e - manually edit the current hunk
   ? - print help
```
