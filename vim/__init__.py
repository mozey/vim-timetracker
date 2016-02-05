command_result = ""


def command():
    return command_result


class Buffer:
    buf = {}

    def __init__(self):
        pass

    def append(self, s, cl):
        self.buf[cl] = s

buf = Buffer()


class Window:

    def __init__(self):
        pass

    cursor = [None, None]

window = Window()


class Current:

    def __init__(self, line=None):
        self.window = window
        self.buffer = buf
        self.line = line


current = Current()


