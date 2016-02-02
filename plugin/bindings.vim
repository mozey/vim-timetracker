" ..............................................................................
" TimeTracker

" Date
nmap <C-t>d a<C-R>=strftime("%Y-%m-%d")<CR><Esc>
imap <C-t>d <C-R>=strftime("%Y-%m-%d")<CR>

" Time
nmap <C-t>t :call TTTime()<Esc>
imap <C-t>t <C-o>:call TTTime()<CR>

" Time Row
nmap <C-t>r :call TTRow()<CR>
imap <C-t>r <C-o>:call TTRow()<CR>

" Sum Block
nmap <C-t>b :call TTBlock()<CR>

" Sum Day
nmap <C-t>s :call TTSum()<CR>

" All Days
nmap <C-t>a :call TTAll()<CR>

" ..............................................................................
" Header

" One =
nmap <C-h>1 :call HOne()<Esc>
imap <C-h>1 <C-o>:call HOne()<CR>