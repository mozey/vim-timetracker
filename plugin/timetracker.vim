function! Tt_block()
python <<EOF

import math
import re
import vim

def get_tab():
    # 4 spaces
    return "    "

def get_totals(a_rows):
    a_totals = []
    for n in range(0, len(a_rows)):
        a_rows[n] = re.sub(r"\s+", "", a_rows[n])
        s_total = a_rows[n].split("->")[1]
        a_totals.append(s_total)
    return a_totals

def sum_totals(a_rows):
    a_totals = get_totals(a_rows)
    n_hours = 0
    n_minutes = 0
    for n in range(0, len(a_totals)):
        n_hours += int(math.floor((float(a_totals[n][:2]))))
        n_minutes += int(math.floor((float(a_totals[n][3:5]))))
    if n_minutes >= 60:
        n_hours += int(math.floor((n_minutes / 60)))
        n_minutes %= 60

    if n_hours < 10:
        s_hours = "0" + str(n_hours)
    else:
        s_hours = str(n_hours)

    if n_minutes < 10:
        s_minutes = "0" + str(n_minutes)
    else:
        s_minutes = str(n_minutes)
    return s_hours + ":" + s_minutes

window = vim.current.window
b = vim.current.buffer
cl, cc = window.cursor

rows_to_sum = []
for l in range(cl - 1, 0, -1):
    if len(b[l]) > 0:
        if b[l][0] == "=":
            # task = b[l]
            break
        else:
            rows_to_sum.append(b[l])

line = "=> " + sum_totals(rows_to_sum)

# Insert tab at beginning of line of there is none
tab = get_tab()
regex = re.compile("^" + tab)
if not re.match(regex, line):
    line = tab + line

b[cl - 1] = line

EOF
endfunction

function! Tt_h_one()
python <<EOF

"""
Prepend current line with header 1
"""
import vim
import re
vim.current.line = re.sub(r"^#*\s*", "", vim.current.line)
vim.current.line = "# " + vim.current.line

EOF
endfunction

function! Tt_h_two()
python <<EOF

"""
Prepend current line with header 2
"""
import vim
import re
vim.current.line = re.sub(r"^#*\s*", "", vim.current.line)
vim.current.line = "## " + vim.current.line

EOF
endfunction

function! Tt_row()
python <<EOF

from datetime import datetime
import re
import vim

def get_tab():
    # 4 spaces
    return "    "

def get_date_time(s_time):
    a_time = s_time.split(":")
    a_time[0] = int(a_time[0])
    a_time[1] = int(a_time[1])
    today = datetime.today()
    date_time = datetime(
        today.year, today.month, today.day, a_time[0], a_time[1]
    )
    return date_time

def time_elapsed(s):
    s = re.sub(r"\s+", "", s)
    a_time = s.split("-")
    t1 = get_date_time(a_time[0])
    t2 = get_date_time(a_time[1])
    d = t2 - t1

    n_hours = d.seconds / (60 * 60)
    n_minutes = (d.seconds % (60 * 60)) / 60

    if n_hours < 10:
        s_hours = "0" + str(n_hours)
    else:
        s_hours = str(n_hours)

    if n_minutes < 10:
        s_minutes = "0" + str(n_minutes)
    else:
        s_minutes = str(n_minutes)

    return a_time[0] + " - " + a_time[1] + \
        " -> " + s_hours + ":" + s_minutes

window = vim.current.window
vim.current.line = get_tab() + time_elapsed(vim.current.line)
l, c = window.cursor
window.cursor = (l, 23)

EOF
endfunction

function! Tt_sum()
python <<EOF

import math
import re
import vim

def get_totals(a_rows):
    a_totals = []
    for n in range(0, len(a_rows)):
        a_rows[n] = re.sub(r"\s+", "", a_rows[n])
        a_total = a_rows[n].split("->")
        if len(a_total) > 1:
            a_totals.append(a_total[1])
    return a_totals

def sum_totals(s):
    a_totals = get_totals(s)
    n_hours = 0
    n_minutes = 0
    for n in range(0, len(a_totals)):
        n_hours += int(math.floor(float(a_totals[n][:2])))
        n_minutes += int(math.floor(float(a_totals[n][3:5])))
    if n_minutes >= 60:
        n_hours += int(math.floor(n_minutes / 60))
        n_minutes %= 60

    if n_hours < 10:
        s_hours = "0" + str(n_hours)
    else:
        s_hours = str(n_hours)
    if n_minutes < 10:
        s_minutes = "0" + str(n_minutes)
    else:
        s_minutes = str(n_minutes)

    return s_hours + ":" + s_minutes

window = vim.current.window
b = vim.current.buffer
cl, cc = window.cursor

rows_to_sum = []
for l in range(cl - 1, 0, -1):
    if len(b[l]) > 0:
        if b[l][0:4] == "#":
            # header = b[l - 1]
            break
        else:
            rows_to_sum.append(b[l])

b[cl - 1] = "==> " + sum_totals(rows_to_sum)

EOF
endfunction

function! Tt_time()
python <<EOF

from datetime import datetime
import math
import vim
import re

def get_tab():
    # 4 spaces
    return "    "

def get_time():
    now = datetime.today()
    s_hours = str(now.hour)
    s_minutes = str(now.minute)

    if len(s_hours) == 1:
        s_hours = "0" + str(s_hours)

    if len(s_minutes) == 1:
        s_minutes = "0" + str(s_minutes)

    s_min_digit_1 = s_minutes[0]
    s_min_digit_2 = s_minutes[1]
    s_min_digit_2 = str(
            int(math.floor((round(float(s_min_digit_2) / 5) * 5)))
    )

    if s_min_digit_2 == "10":
        if s_min_digit_1 == "5":
            if s_hours == "23":
                s_hours = "00"
                s_minutes = "00"
            else:
                s_hours = str(int(s_hours) + 1)
                s_minutes = "00"
        else:
            s_min_digit_1 = str(int(s_min_digit_1) + 1)
            s_minutes = s_min_digit_1 + "0"
    else:
        s_minutes = s_min_digit_1 + s_min_digit_2

    return s_hours + ":" + s_minutes

window = vim.current.window
l, c = window.cursor
line = vim.current.line
i = c + 1
vim.current.line = line[:i] + get_time() + line[i:]

# Insert tab at beginning of line of there is none
tab = get_tab()
regex = re.compile("^" + tab)
if not re.match(regex, vim.current.line):
    vim.current.line = tab + vim.current.line

window.cursor = (l, c + 5)

EOF
endfunction

