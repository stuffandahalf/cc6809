# -*- coding: utf-8 -*-

class Type(object):
    def __init__(self, key, size):
        self.key = key
        self.size = size
        
        self.expr = key.split()
        for i in range(0, len(self.expr)):
            if self.expr[i] == 'int' and len(self.expr) != 1:
                self.expr[i] = r'\(int|\B\)'
        self.expr = r'\w+'.join(self.expr)
        #print self.expr
    
    def regex(self):
        return re.compile(self.key)
    
    def __str__(self):
        return 'Regex: ' + self.expr + ' Size: ' + str(self.size)
    
    def __repr__(self):
        return 

def PTR(): return Type('*', 2)
def VOID(): return Type('void', 0)
def CHAR(): return Type('char', 1)
def INT(): return Type('int', 2)
def LONG_INT(): return Type('long int', 4)
def LONG_LONG_INT(): return Type('long long int', 8)
def FLOAT(): return Type('float', 2)
def DOUBLE(): return Type('double', 4)
def LONG_DOUBLE(): return Type('long double', 8)

types = [
    #VOID(),
    CHAR(),
    INT(),
    LONG_INT(),
    LONG_LONG_INT(),
    FLOAT(),
    DOUBLE(),
    LONG_DOUBLE()
]
