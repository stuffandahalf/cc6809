#!/usr/bin/env python
# -*- coding: utf-8 -*-

from preprocessor import *
from types import *
from function import Function

lib = "./lib/"

functions = []
global_vars = []

def main(args):
    if len(args) < 2:
        return 1
    cfile = open(args[1], 'r')
    code = clean(cfile)
    
    Preprocesser(code)
    #print code
    
    cfile.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
