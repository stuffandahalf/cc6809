class Scope(object):
    def __init__(self, from_line, to_line):
        self.typedefs = []
        self.ops = []
        self.from_line = from_line
        self.to_line = to_line

class Typedef(object):
    def __init__(self, line, value):
        self.line = line
        self.value = value

class If(object):
    def __init__(self, from_line, to_line):
        self.scope = Scope(from_line, to_line)
