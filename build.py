#!/usr/bin/env python

from vim_timetracker import timetracker
import inspect
import os
import re

build_path = os.path.join(
    os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
    ),
    "plugin",
    "timetracker.vim"
)


def write_func(func_name, body):
    f.write("function! ")
    f.write(func_name + "()\n")
    f.write("python <<EOF\n\n")

    f.writelines(body)

    f.write("\nEOF\n")
    f.write("endfunction\n\n")


def add_functions():
    for func_name in dir(timetracker):
        if func_name[0] is not "_":
            func = getattr(timetracker, func_name)
            body, _ = inspect.getsourcelines(func)

            for i in range(len(body)):
                # Remove first level of indentation,
                # assumes four spaces for each level.
                body[i] = re.sub(r"^\s{4}", "", body[i])

            write_func(func_name.capitalize(), body[1:])
            print(func_name + "...")


with open(build_path, "w+") as f:
    add_functions()
