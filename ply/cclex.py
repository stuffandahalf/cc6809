# -*- coding: utf-8 -*-

import ply.lex as lex

tokens = [
    'NAME',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS'
]

t_ignore = ' \t'
#t_error = 'Error'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_error(t):
    print "Illegal character %s" % t.value[0]
    t.lexer.skip(1)

lex.lex(debug = 0)

#str = "int x = 5"
# str = "x = 5"
# lex.input(str);
# while True:
        # tok = lex.token()
        # if not tok:
            # break;
        # print tok
        
