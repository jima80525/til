# Reload vimrc File Without Restarting

To reload the vimrc file you are editing a single time, use:

    :so %

To configure vim to auto-reload every time it is saved, add this to your vimrc
file

```vimL
" auto-reload vimrc when saving
augroup vimrc     " Source vim configuration upon save
  autocmd! BufWritePost jima.vimrc source % | echom "Reloaded " . $MYVIMRC | redraw
  autocmd! BufWritePost $MYVIMRC source % | echom "Reloaded " . $MYVIMRC | redraw
  autocmd! BufWritePost $MYGVIMRC if has('gui_running') | so % | echom "Reloaded " . $MYGVIMRC | endif | redraw
augroup END
```
