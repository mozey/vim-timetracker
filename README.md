# timetracker

Vim plugin written in python for flat-file todo list time sheets


## Installation

Vim must be compiled with 
[python support](http://stackoverflow.com/questions/13477264/import-vim-in-python-gives-back-errors)

Requires [vim-plug](https://github.com/junegunn/vim-plug)

    curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    
Add timetracker to ~/.vimrc
 
    call plug#begin()
    Plug 'mozey/vim-timetracker'
    call plug#end()
    
And install with plug

    :PlugInstall
    
TODO :PlugUpdate doesn't seem to work? To update:
 
    rm -rf ~/.vim/plugged/vim-timetracker
    
    vim 
    
    :PlugInstall


## Debugging

As per the [official docs](http://vimdoc.sourceforge.net/htmldoc/if_pyth.html)

Use `:pyfile myscript.py`


## Testing

TODO `test.py`

Manual testing

    cp ./plugin/bindings.vim ~/.vim/plugged/vim-timetracker/plugin/bindings.vim
    
    cp ./plugin/timetracker.vim ~/.vim/plugged/vim-timetracker/plugin/timetracker.vim
    

## Disclaimer

It's very likely that no-one besides myself will find this useful, just uploaded 
it to github for backup and in an attempt to document my workflow for myself.


## Why?

For many years I kept a `todo.txt` on my computer. I would prefix these with the
year and month, for example, `2016-01 todo.txt`. At some point I switched to 
using markdown so the files became `2016-02 todo.md`. Usually I would edit them 
with whatever text editor was available on the OS I was currently using, for a 
while now that text editor has been vim.
 
Many many times I've pondered using an actual database for this, and maybe I 
will at some point. I've also used various other text file based todo scripts 
and programs, but I find I keep coming back to using just a simple editable 
file, even though it's somewhat clunky.

A couple of years ago I wrote __two vim plugins__ in python that helps me 
maintain the todo text files, this repos is a combination of these two plugins:


### header.vim

Make two different kinds of headers

    # First kind
    
    ## Second kind

### timetracker.vim

Insert current date

    2016-02-02

Insert current time rounded to nearest 5 minutes

    09:25

Calculate time difference in hh:mm

    09:00 - 09:25 -> 00:25

Sum time diffs for a block

    => 01:30

Sum time diffs for the entire day

    ==> 07:00


## Example

The content of `2016-01 todo.txt` might look like this
    
    # 2016-02-02
    
    ## My Project
    
    * Task 1
    * Sub task of task 1
    * Random note
    
    09:00 - 09:25 -> 00:25
    10:00 - 10:15 -> 00:15
    11:10 - 12:00 -> 00:50
    => 01:30
    
    * Task 2
    
    09:25 - 10:00 -> 00:35
    => 00:35
    
    * Task 3
    * Sub task of task 3
    
    10:15 - 11:10 -> 00:55
    12:00 - 13:00 -> 01:00
    => 01:55
    
    My Other Project
    ----------------
    
    * Task 1
    
    14:00 - 17:00 -> 03:00
    => 03:00
    
    ==> 07:00


## TODO 

Some good tips for improvement here,
[Writing Vim Plugins in Python](http://www.terminally-incoherent.com/blog/2013/05/06/vriting-vim-plugins-in-python/)
especially the bit about failing silently when vim doesn't have Python support.

More documentation here [Scripting Vim with Python](http://orestis.gr/blog/2008/08/10/scripting-vim-with-python/)

The contents of the `test` folder has to be revised
