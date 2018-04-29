#!/usr/bin/env python
# -*- coding: utf-8 -*-

from expressions import *
from scope import Scope
from data_types import types
#import asm

glob_scope = None

def build_ast(code):
    code = code.split('\n')
    #for line_num in range(0, len(code)):
    line_num = 0
    print code[line_num]
    match = FUNCTION_EXPR().match(code[line_num])
    print match
    if match != None:
        print match.group('func_type')
        #pass

def main(args):
    if len(args) < 2:
        print 'Insufficient arguments'
        print 'Usage: ./cc6809 file.c'
        return 1
    
    cfile = open(args[1], 'r');
    if cfile == None:
        print 'Failed to open source file'
        return 1
        
    code = cfile.read().strip()
    
    build_ast(code)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
