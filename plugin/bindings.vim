" ..............................................................................
" TimeTracker

" Date
nmap <C-t>d a<C-R>=strftime("%Y-%m-%d")<CR><Esc>
imap <C-t>d <C-R>=strftime("%Y-%m-%d")<CR>

" Time
nmap <C-t>t :call Tt_time()<Esc>
imap <C-t>t <C-o>:call Tt_time()<CR>

" Time Row
nmap <C-t>r :call Tt_row()<CR>
imap <C-t>r <C-o>:call Tt_row()<CR>

" Sum Block
nmap <C-t>b :call Tt_block()<CR>

" Sum Day
nmap <C-t>s :call Tt_sum()<CR>

" All Days
nmap <C-t>a :call Tt_all()<CR>

" Header Next
nmap <C-h>n :call Tt_h_next()<Esc>
imap <C-h>n <C-o>:call Tt_h_next()<CR>

" Header 1
nmap <C-h>1 :call Tt_h_one()<Esc>
imap <C-h>1 <C-o>:call Tt_h_one()<CR>

" Header 2
nmap <C-h>2 :call Tt_h_two()<Esc>
imap <C-h>2 <C-o>:call Tt_h_two()<CR>

