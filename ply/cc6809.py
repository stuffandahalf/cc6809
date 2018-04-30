#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ccparse

def main(args):
    #if len(args) < 2:
    #    print 'insufficient arguments'
    #    print 'Usage:\t./cc6809 fname.c'
    #    return 1
    
    prog = ccparse.parse('x = 5')
    print prog
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
