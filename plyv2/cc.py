#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Function to print to stderr
from __future__ import print_function
import sys

# Argument parser
from argparse import ArgumentParser

# Import lexer and parser
import cclex
import ccyacc

def eprint(*args, **kwargs):
    '''
    Prints input to stderr
    '''
    print(*args, file=sys.stderr, **kwargs)

# Main function
def main(args):
    #print cclex.tokens
    
    #if len(args) < 2:
        #eprint('Missing arguments.')
        #eprint('usage: ./cc6809.py filename.c')
        #return 1
    
    c_file = open('../test_files/kern_add_test.c', 'r')
    code = c_file.read()
    cclex.lexer.input(code)
    while 1:
        tok = cclex.lexer.token()
        if not tok: break
        print(tok)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
