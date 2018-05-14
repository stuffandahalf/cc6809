#!/usr/bin/env python
# -*- coding: utf-8 -*-

# C Preprocessor

#import cpplex
#import cppparse

from cppparser import CPP

parser = CPP()

def main(args):
    # if len(args) < 2:
        # print 'Insufficient arguments'
        # print 'Usage:\tcpp6809.py fname.c'
        # return 1
    
    filepath = '../test_files/test1.c'
    cfile = open(filepath, 'r')
    code = cfile.read().strip()
    
    test = '#include <stdio.h>'
    parser.parse(test, 1)

    #parser.parse(code, 1)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
