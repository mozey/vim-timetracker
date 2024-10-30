#!/usr/bin/env python3

# Export all todos to csv

import sys
import os
import time
import datetime
from collections import OrderedDict
import csv

"""
Export file header:
"""
header = ["date", "project", "tasks", "seconds", "total", "fixed_amount"]
currency = ["$", "R"]

if len(sys.argv) != 3:
    print("USAGE:")
    print("    export_csv.py SOURCE DESTINATION")
    exit()

source = sys.argv[1]
destination = sys.argv[2]

if destination == source:
    print("Destination and source must not be the same")
    sys.exit(1)

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
response = [header]


def reset_state():
    state["project"] = None
    state["date"] = None
    state["tasks"] = []
    state["task_seconds"] = 0
    state["task_total"] = ""
    state["fixed_amount"] = 0


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

    # Task spans two days
    if diff < 0:
        d1 = datetime.datetime(1, 1, 1, int(t1[0]), int(t1[1]), 00)
        d2 = datetime.datetime(1, 1, 2, int(t2[0]), int(t2[1]), 00)
        diff = int((d2 - d1).total_seconds())

    state["task_seconds"] += diff


skip_lines = False


def process_line(line, callback):
    global skip_lines
    global currency
    line = line.replace("\n", "")
    line = line.lstrip()

    def check_total():
        if state["task_seconds"] != 0:
            callback()
        elif state["fixed_amount"] != 0:
            callback()
        else:
            return
        state["tasks"] = []
        state["task_seconds"] = 0
        state["task_total"] = ""
        state["fixed_amount"] = 0

    if len(line) > 0:
        # print(line)
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

        elif line[:3] == "=x ":
            # Skip tasks starting with "=x "
            skip_lines = True

        elif line[:1] in currency:
            state["fixed_amount"] = line

        elif is_number(line[:2]):
            if not skip_lines:
                sum_task_total(line)

        elif is_number(line[:1]):
            # Hours is only one digit
            raise Exception(
                "Time slip rows must have format hh:mm => {}".format(line))


def process_file():
    with open(source, "r") as f:
        def flush():
            # Appends task to time_slips
            state["task_total"] = sec_to_str(state["task_seconds"])
            response.append([
                state["date"],
                state["project"],
                " | ".join(state["tasks"]),
                state["task_seconds"],
                state["task_total"],
                state["fixed_amount"]
            ])

        lines = f.readlines()
        for line in lines:
            process_line(line, flush)
            # print(line)

        if state["task_total"] != 0:
            flush()

process_file()

# with open(destination, "w+") as f:
#     # print(json.dumps(response, indent=2))
#     json.dump(response, f, indent=2)

with open(destination, "w", newline='') as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerows(response)
