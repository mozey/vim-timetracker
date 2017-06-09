#!/usr/bin/env python

# Export all todos to json

# Maybe this should also be a callable from vim,
# just a plain python script for now.

"""

Export file structure:

{
    "file_path": "/path/to/todo.md",
    "time_slips": [
        {
            "project": "My project",
            "date": "2016-02-05",
            "tasks": ["There can be more than one task per time slip"],
            "total": "03:35",
            "seconds": "12300"
        }
    ],
    "projects": {
        "My Project": {
            "total": "03:15",
            "seconds": "12300"
        }
    }
}

"""

import sys
import os
import time
import datetime
from collections import OrderedDict
import copy
import json


if len(sys.argv) != 3:
    print("USAGE:")
    print("    export_json.py SOURCE DESTINATION")
    exit()

source = sys.argv[1]
destination = sys.argv[2]

filter_project = None
if len(sys.argv) == 4:
    filter_project = sys.argv[4]

if not os.path.exists(source):
    print("Source does not exist")
    exit()


# TODO The timetracker.py should also use these two functions?
def sec_to_str(s):
    return time.strftime('%H:%M', time.gmtime(s))


def str_to_sec(s):
    x = time.strptime(s, '%H:%M')
    return datetime.timedelta(
            hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec
    ).total_seconds()


state = OrderedDict()
response = OrderedDict()
response["file_path"] = ""
response["time_slips"] = []
response["projects"] = {}


def reset_state():
    state["project"] = None
    state["date"] = None
    state["tasks"] = []
    state["task_seconds"] = 0
    state["task_total"] = ""


reset_state()


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def sum_task_total(line):
    # TODO Use regex to extract time strings
    t1 = line[:5].split(":")
    t2 = line[8:13].split(":")

    d1 = datetime.datetime(1, 1, 1, int(t1[0]), int(t1[1]), 00)
    d2 = datetime.datetime(1, 1, 1, int(t2[0]), int(t2[1]), 00)
    diff = int((d2 - d1).total_seconds())

    state["task_seconds"] += diff


skip_lines = False


def process_line(line, callback):
    global skip_lines
    line = line.replace("\n", "")
    line = line.lstrip()

    def check_total():
        if state["task_seconds"] != 0:
            callback()
            state["tasks"] = []
            state["task_seconds"] = 0
            state["task_total"] = ""

    if len(line) > 0:
        if line[:2] == "# ":
            check_total()
            reset_state()
            state["date"] = line[2:]

        elif line[:3] == "## ":
            check_total()
            state["project"] = line[3:]
            state["tasks"] = []

        elif line[:2] == "= ":
            check_total()
            state["tasks"].append(line[2:])
            skip_lines = False

        elif line[:3] == "== ":
            # Skip tasks starting with "== "
            skip_lines = True

        elif is_number(line[:2]):
            if not skip_lines:
                sum_task_total(line)


def process_file():
    with open(source, "r") as f:
        def flush():
            # Appends task to time_slips
            state["task_total"] = sec_to_str(state["task_seconds"])
            response["time_slips"].append(copy.deepcopy(state))

            if state["project"] not in response["projects"]:
                # Create project
                project = OrderedDict()
                project["seconds"] = state["task_seconds"]
                project["total"] = state["task_total"]
                response["projects"][state["project"]] = project

            else:
                # Update project
                project = response["projects"][state["project"]]
                project["seconds"] += state["task_seconds"]
                project["total"] = sec_to_str(project["seconds"])

        lines = f.readlines()
        for line in lines:
            process_line(line, flush)
            # print(line)

        if state["task_total"] != 0:
            flush()

process_file()

with open(destination, "w+") as f:
    # print(json.dumps(response, indent=2))
    json.dump(response, f, indent=2)
