#function TTRow()
#python <<EOF
#
#from datetime import datetime
#import re
#import vim
#
#def fGetDateTime(sTime):
#    aTime = sTime.split(":")
#    aTime[0] = int(aTime[0])
#    aTime[1] = int(aTime[1])
#    Today = datetime.today();
#    DateTime = datetime(Today.year, Today.month, Today.day, aTime[0], aTime[1])
#    return DateTime
#
#def fTimeElapsed(s):
#    s = re.sub(r"\s+", "",  s)
#    aTime = s.split("-")
#    t1 = fGetDateTime(aTime[0])
#    t2 = fGetDateTime(aTime[1])
#    d = t2 - t1
#
#    nHours = d.seconds / (60 * 60)
#    nMinutes = (d.seconds % (60 * 60)) / 60
#
#    if (nHours < 10):
#        sHours = "0" + str(nHours)
#    else:
#        sHours = str(nHours)
#
#    if (nMinutes < 10):
#        sMinutes = "0" + str(nMinutes)
#    else:
#        sMinutes = str(nMinutes)
#
#    return aTime[0] + " - " + aTime[1] + " -> " + sHours + ":" + sMinutes;
#
#window = vim.current.window
#vim.current.line = fTimeElapsed(vim.current.line);
#l, c = window.cursor
#window.cursor = (l, 23)
#
#EOF
#endfunction
#
#function TTTime()
#python <<EOF
#
#from datetime import datetime
#import math
#import vim
#
#def fGetTime():
#    Now = datetime.today()
#    sHours = str(Now.hour)
#    sMinutes = str(Now.minute)
#
#    if (len(sHours) == 1):
#        sHours = "0" + str(sHours)
#
#    if (len(sMinutes) == 1):
#        sMinutes = "0" + str(sMinutes)
#
#    sMinDigit1 = sMinutes[0]
#    sMinDigit2 = sMinutes[1]
#    sMinDigit2 = str(int(math.floor((round(float(sMinDigit2) / 5) * 5))));
#
#    if (sMinDigit2 == "10"):
#        if (sMinDigit1 == "5"):
#            if (sHours == "23"):
#                sHours = "00"
#                sMinutes = "00"
#            else:
#                sHours = str(int(sHours) + 1)
#                sMinutes = "00"
#        else:
#            sMinDigit1 = str(int(sMinDigit1) + 1)
#            sMinutes = sMinDigit1 + "0"
#    else:
#        sMinutes = sMinDigit1 + sMinDigit2
#
#    return sHours + ":" + sMinutes;
#
#window = vim.current.window
#l, c = window.cursor
#line = vim.current.line
#i = c + 1
#vim.current.line = line[:i] + fGetTime() + line[i:]
#window.cursor = (l, c + 5)
#
#EOF
#endfunction
#

def TTBlock(vim):
    import math
    import re

    def fGetTotals(aRows):
        aTotals = []
        for n in range(0, len(aRows)):
            aRows[n] = re.sub(r"\s+", "", aRows[n])
            sTotal = aRows[n].split("->")[1]
            aTotals.append(sTotal)
        return aTotals

    def fSumTotals(aRows):
        aTotals = fGetTotals(aRows)
        nHours = 0
        nMinutes = 0
        for n in range(0, len(aTotals)):
            nHours += int(math.floor((float(aTotals[n][:2]))))
            nMinutes += int(math.floor((float(aTotals[n][3:5]))))
        if (nMinutes >= 60):
            nHours += int(math.floor((nMinutes / 60)))
            nMinutes = nMinutes % 60
        if (nHours < 10):
            sHours = "0" + str(nHours)
        else:
            sHours = str(nHours)
        if (nMinutes < 10):
            sMinutes = "0" + str(nMinutes)
        else:
            sMinutes = str(nMinutes)
        return sHours + ":" + sMinutes

    window = vim.current.window
    b = vim.current.buffer
    cl, cc = window.cursor

    aRows = []
    for l in range(cl - 1, 0, -1):
        if len(b[l]) > 0:
            if b[l][0] == "*":
                task = b[l]
                break
            else:
                aRows.append(b[l])

    b[cl - 1] = "=> " + fSumTotals(aRows)


def TTSum(vim):
    import math
    import re

    def fGetTotals(aRows):
        aTotals = []
        for n in range(0, len(aRows)):
            aRows[n] = re.sub(r"\s+", "", aRows[n])
            aTotal = aRows[n].split("->")
            if len(aTotal) > 1:
                aTotals.append(aTotal[1])
        return aTotals

    def fSumTotals(s):
        aTotals = fGetTotals(s)
        nHours = 0
        nMinutes = 0
        for n in range(0, len(aTotals)):
            nHours += int(math.floor(float(aTotals[n][:2])))
            nMinutes += int(math.floor(float(aTotals[n][3:5])))
        if nMinutes >= 60:
            nHours += int(math.floor(nMinutes / 60))
            nMinutes = nMinutes % 60
        if nHours < 10:
            sHours = "0" + str(nHours)
        else:
            sHours = str(nHours)
        if nMinutes < 10:
            sMinutes = "0" + str(nMinutes)
        else:
            sMinutes = str(nMinutes)
        return sHours + ":" + sMinutes

    window = vim.current.window
    b = vim.current.buffer
    cl, cc = window.cursor

    aRows = []
    for l in range(cl - 1, 0, -1):
        if len(b[l]) > 0:
            if b[l][0:4] == "====":
                header = b[l - 1]
                break
            else:
                aRows.append(b[l])

    b[cl - 1] = "==> " + fSumTotals(aRows)


def TTAll(vim):
    import math
    import re

    def fGetTotals(aRows):
        aTotals = []
        for n in range(0, len(aRows)):
            aRows[n] = re.sub(r"\s+", "", aRows[n])
            aTotal = aRows[n].split("==>")
            if len(aTotal) > 1:
                aTotals.append(aTotal[1])
        return aTotals

    def fSumTotals(s):
        aTotals = fGetTotals(s)
        nHours = 0
        nMinutes = 0
        for n in range(0, len(aTotals)):
            nHours += int(math.floor(float(aTotals[n][:2])))
            nMinutes += int(math.floor(float(aTotals[n][3:5])))
        if nMinutes >= 60:
            nHours += int(math.floor(nMinutes / 60))
            nMinutes = nMinutes % 60
        if nHours < 10:
            sHours = "0" + str(nHours)
        else:
            sHours = str(nHours)
        if nMinutes < 10:
            sMinutes = "0" + str(nMinutes)
        else:
            sMinutes = str(nMinutes)
        return sHours + ":" + sMinutes

    window = vim.current.window
    b = vim.current.buffer
    cl, cc = window.cursor

    aRows = []
    for l in range(cl - 1, 0, -1):
        if len(b[l]) > 0:
            if b[l][0:3] == "==>":
                aRows.append(b[l])

    b[cl - 1] = "===> " + fSumTotals(aRows)


class current:
    def __init__(self, window, buffer):
        self.window = window
        self.buffer = buffer

class window:
    def __init__(self, cursor):
        self.cursor = cursor

class vim:
    def __init__(self, cursor, buffer):
        self.current = current(window(cursor), buffer)

v = vim(
    (),
    [
        "2012-07-13",
        "==========",
        "",
        "* Do something",
        "09:40 - 10:40 -> 01:00",
        "12:00 - 12:45 -> 00:45",
        "",
        "",
        "",
        "* Another task",
        "08:00 - 10:15 -> 02:15",
        "12:00 - 13:00 -> 01:00",
        "",
        "",
        "==> 06:09",
        ""
    ]
)

v.current.window.cursor = (7, 0)
TTBlock(v)
print v.current.buffer
print "Pass: " + str(v.current.buffer[6] == "=> 01:45")

v.current.window.cursor = (13, 0)
TTBlock(v)
print v.current.buffer
print "Pass: " + str(v.current.buffer[12] == "=> 03:15")

v.current.window.cursor = (14, 0)
TTSum(v)
print v.current.buffer
print "Pass: " + str(v.current.buffer[13] == "==> 05:00")

v.current.window.cursor = (16, 0)
TTAll(v)
print v.current.buffer
print "Pass: " + str(v.current.buffer[15] == "===> 11:09")
