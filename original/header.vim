" =============================================================================
" Functions

function! HOne()
python <<EOF

import vim

def fRepeat(s, n):
    r = ""
    for i in range(0, n):
      r += s
    return r

window = vim.current.window
b = vim.current.buffer
cl, cc = window.cursor

line = vim.current.line
length = len(line)
if length < 4: length = 4
header = fRepeat("=", length)
b.append(header, cl)

EOF
endfunction

function! HTwo()
python <<EOF

import vim

def fRepeat(s, n):
    r = ""
    for i in range(0, n):
      r += s
    return r

window = vim.current.window
b = vim.current.buffer
cl, cc = window.cursor

line = vim.current.line
length = len(line)
if length < 4: length = 4
header = fRepeat("-", length)
b.append(header, cl)

EOF
endfunction

" =============================================================================
" Syntax

au BufRead,BufNewFile *.txt hi header1 guifg=#FF7F50
au BufRead,BufNewFile *.txt syn match header1 /\*\*\*.*$/

au BufRead,BufNewFile *.txt hi header2 guifg=#B8860B
au BufRead,BufNewFile *.txt syn match header2 /===.*$/

au BufRead,BufNewFile *.txt hi header3 guifg=#8FBC8F
au BufRead,BufNewFile *.txt syn match header3 /\-\-\-.*$/


