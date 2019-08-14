#!/usr/bin/env python

from vim_timetracker import timetracker

import vim
vim.current.line = "    09:30 - 13:10"

timetracker.tt_row()
assert vim.current.line == "    09:30 - 13:10 -> 03:40"

