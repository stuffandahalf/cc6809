#from data_types import types
#import data_types
from data_types import *
import re

def IDENTIFIER(): return r'[a-zA-Z][a-zA-Z0-9]*'

def DATA_TYPE_EXPR():
    expr = r'\('
    for i in range(0, len(types)):
        if i > 0:
            expr += r'|'
        expr += types[i].expr
    expr += r'\)'
    #print expr
    return expr

def FUNCTION_EXPR():
    #expr = r'\A(?P<func_type>' + DATA_TYPE_EXPR() + r')\w+(?P<func_name>.*)'#\w*(' + DATA_TYPE_EXPR() + r'
    #funcdef = r'\A(?P<func_type>' + DATA_TYPE_EXPR() + r')\w+(?P<func_name>' + IDENTIFIER() + ')'
    #args = r'\((?P<args>(' + DATA_TYPE_EXPR() + r'\w+' + IDENTIFIER() + '\w+'
    #expr = r'\A(?P<func_type>' + DATA_TYPE_EXPR() + r')\w+(?P<func_name>' + IDENTIFIER() + ')\w+\((?P<arguments>(' + DATA_TYPE_EXPR() + r'\w+' + IDENTIFIER() + ')*)\)'
    #args = r'\((?P<args>((' + DATA_TYPE_EXPR() + r'\w+' + IDENTIFIER() + ',\w+)*(' + DATA_TYPE_EXPR() + r'\w+' + IDENTIFIER() + ').*))\)'
    funcdef = r'\A(?P<func_type>' + DATA_TYPE_EXPR() + r')'
    #args = r'\((?P<args>(((' + DATA_TYPE_EXPR() + '\s+' + IDENTIFIER() + '\s*,)*' + DATA_TYPE_EXPR() + '\s+' + IDENTIFIER() + ')|\B)\))'
    #args = r'\((?P<args>.*)\)'
    args = r'((?P<args>\(\B\)))'
    print args
    expr = funcdef + r'\s+' + args + r'\s+'
    #print expr
    return re.compile(expr)
