#!/usr/bin/env python

from vim_timetracker import timetracker

import vim
vim.current.line = "foo"

timetracker.tt_h_one()
assert vim.current.line == "# foo"

timetracker.tt_h_two()
assert vim.current.line == "## foo"






