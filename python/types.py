modifiers = ['unsigned', 'static']
types = ['byte', 'short', 'char', 'struct']

class Type(object):
    def __init__(type, data):
        self.type = type
        self.data = data
