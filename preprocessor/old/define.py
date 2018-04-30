# -*- coding: utf-8 -*-

class Define(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self):
        return self.value
    
    def __str__(self):
        pass
