def HOne(vim):

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


def HTwo(vim):

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

class Current:
    def __init__(self, window, buffer):
        self.window = window
        self.buffer = buffer
        self.set_line()

    def set_line(self):
        self.line = self.buffer[self.window.cursor[0] - 1]

class Window:
    def __init__(self, cursor):
        self.cursor = cursor

class Buffer(list):
    def __init__(self, myList):
        for item in myList:
            super(Buffer, self).append(item)

    def append(self, item, cl):
        # Insert new item at position cl
        super(Buffer, self).insert(cl, item)

        # This is the normal behaviour of append
        #super(Buffer, self).append(item)

class Vim:
    def __init__(self, cursor, buffer):
        self.current = Current(Window(cursor), Buffer(buffer))

v = Vim(
    (1, 0),
    [
        "Header 1",
        "Header 2",
        "He",
    ]
)

v.current.window.cursor = (1, 0)
v.current.set_line()
HOne(v)
print v.current.buffer
print "Pass: " + str(v.current.buffer[1] == "========")

v.current.window.cursor = (3, 0)
v.current.set_line()
HTwo(v)
print v.current.buffer
print "Pass: " + str(v.current.buffer[3] == "--------")

v.current.window.cursor = (5, 0)
v.current.set_line()
HTwo(v)
print v.current.buffer
print "Pass: " + str(v.current.buffer[5] == "----")
