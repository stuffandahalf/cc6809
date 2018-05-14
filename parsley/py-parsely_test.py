#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import data_types
#from expressions import *
import parsley

#identifier = [a-zA-Z_][a-zA-Z0-9_]*
#data_type = "'int' | 'char'"

#data_type = "'int'"



def main(args):
    #if len(args) < 2:
        #print 'Insufficient arguments'
        #print 'Usage: ./cc6809 fname.c'
        #return 1
    
    fname = '../test_files/test1.c'
    cfile = open(fname, 'r')
    code = cfile.read()
    
    #print code
    #print grammar("17-34").expr()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
