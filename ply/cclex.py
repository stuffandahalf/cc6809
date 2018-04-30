# Written by Gregory Norton
# Based on https://github.com/dabeaz/ply/blob/master/example/ansic/clex.py

# -*- coding: utf-8 -*-

import ply.lex as lex

reserved = (
    'AUTO', 'BREAK', 'CASE', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT',
    'DO', 'DOUBLE', 'ELSE', 'ENUM', 'EXTERN', 'FLOAT', 'FOR', 'GOTO',
    'IF', 'INT', 'LONG', 'REGISTER', 'RETURN', 'SHORT', 'SIGNED',
    'SIZEOF', 'STATIC', 'STRUCT', 'SWITCH', 'TYPEDEF', 'UNION',
    'UNSIGNED', 'VOID', 'VOLATILE', 'WHILE'
)

#tokens = reserved + (
tokens = (
    # Literals (identifier, integer constant, float constant, string constant,
    # char const)
    'ID', 'TYPEID', 'ICONST', #'FCONST', 'SCONST', 'CCONST',

    # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    #'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
    #'LOR', 'LAND', 'LNOT',
    #'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS', #'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    #'LSHIFTEQUAL', 'RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

    # Increment/decrement (++,--)
    #'PLUSPLUS', 'MINUSMINUS',

    # Structure dereference (->)
    #'ARROW',

    # Conditional operator (?)
    #'CONDOP',

    # Delimeters ( ) [ ] { } , . ; :
    #'LPAREN', 'RPAREN',
    #'LBRACKET', 'RBRACKET',
    #'LBRACE', 'RBRACE',
    #'COMMA', 'PERIOD', 'SEMI', 'COLON',

    # Ellipsis (...)
    #'ELLIPSIS',
)

# Ignore these characters
t_ignore = ' \t\0x0C'

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Operators
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'


# Assignment operators
t_EQUALS = r'='


# Incremenet / Decrement


# ->


# ?


# Delimiters


# Identifiers and reserved words

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r
    
def t_ID(t):
    #r'[A-Za-z_][\w_]*'
    r'[A-Za-z_]\w*'
    t.type = reserved_map.get(t.value, "ID")
    return t
    
#def t_TYPEID(t):
    #r'int | 

t_ICONST = r'\d+'

lex.lex(debug = 0)
