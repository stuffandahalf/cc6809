# -*- coding: utf-8 -*-

class Inst(object):
    def __init__(self, name, opcode, bytes):
        self.name = name
        self.opcode = opcode
        self.bytes = bytes

adc = [
    Inst('ADCA', 0x89, 2),
    Inst('ADCB', 0xC9, 2)
]

cmp = [
    Inst('CMPA', 0x81, 2)
]
