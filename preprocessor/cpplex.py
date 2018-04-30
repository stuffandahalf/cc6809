# -*- coding: utf-8 -*-

import ply.lex as lex

tokens = (
    # #, <. >, "
    #'POUND', 
    'LIBL', 'LIBR', 'QUOTE',
    'INCLUDE', #'IFNDEF', 'ELSE', 'ENDIF',
    'FNAME',
    'COMMENTL', 'COMMENTR', 'COMMENT'
)

t_ignore = ' \t'

# Symbols
#t_POUND = r'\#'
t_LIBL = r'\<'
t_LIBR = r'\>'
t_QUOTE = r'\"'

# Directives
t_INCLUDE = r'\#include'

# Filename
t_FNAME = r'[^\#\<\>\"]+'

# Comments
t_COMMENTL = r'/\*'
t_COMMENTR = r'\*/'
t_COMMENT = r'//'

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)
    
lex.lex(debug=0)
