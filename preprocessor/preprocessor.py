#!/usr/bin/env python
# -*- coding: utf-8 -*-

# regular expressions
import re

# constant include folder location
def LIB(): return '../include'
def INCLUDE_PATTERN(): return re.compile(r'\A\#include\s*(?P<fname>(<|").*(>|")).*')
def DEFINE_MULTI_PATTERN(): return re.compile(r'')
def DEFINE_SINGLE_PATTERN(): return re.compile(r'\A\#define\s+(?P<key>.+)\s')

defines = {}

def parse(code):
    lines = code.split('\n')
    for line_num in range(0, len(lines)):
        if lines[line_num].strip().startswith("#include"):
            #pass
            match = INCLUDE_PATTERN().match(lines[line_num].strip())
            #print match
            #print match.group('fname')
            #lines[line_num] = 
            
        elif lines[line_num].strip().startswith('#define'):
            #pass
            #match = DEFINE_MULTI_PATTERN().match(lines[line_num].strip())
            #if match == None:
            print 'searching for single line'
            match = DEFINE_SINGLE_PATTERN().match(lines[line_num].strip())
            print match
            #print match.group('key')
        #elif
    #print lines
    

def main(args):
    if len(args) < 2: 
        print 'Insufficient arguments'
        print 'Usage: preprocessor filename'
        return 1
    
    cfile = open(args[1], 'r')
    code = cfile.read().strip()
    
    parsed_code = parse(code)
    
    #if parsed_code == :
        
        #return 1
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
