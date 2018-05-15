# -*- coding: utf-8 -*-

import ply.lex as lex

# List of reserved c keywords
reserved = {
    'auto': 'AUTO',
    'break' : 'BREAK',
    'case' : 'CASE',
    'char' : 'CHAR',
    'const' : 'CONST',
    'continue' : 'CONTINUE',
    'default' : 'DEFAULT',
    'do' : 'DO',
    'double' : 'DOUBLE',
    'else' : 'ELSE',
    'enum' : 'ENUM',
    'extern' : 'EXTERN',
    'float' : 'FLOAT',
    'for' : 'FOR',
    'goto' : 'GOTO',
    'if' : 'IF',
    'long' : 'LONG',
    'register' : 'REGISTER',
    'return' : 'RETURN',
    'short' : 'SHORT',
    'signed' : 'SIGNED',
    'sizeof' : 'SIZEOF',
    'static' : 'STATIC',
    'struct' : 'STRUCT',
    'switch' : 'SWITCH',
    'typedef' : 'TYPEDEF',
    'union' : 'UNION',
    'unsigned' : 'UNSIGNED',
    'void' : 'VOID',
    'volatile' : 'VOLATILE',
    'while' : 'WHILE',
    
    '...' : 'ELLIPSIS',
    '>>=' : 'RIGHT_ASSIGN',
    '<<=' : 'LEFT_ASSIGN',
    '+=' : 'ADD_ASSIGN',
    '-=' : 'SUB_ASSIGN',
    '*=' : 'MUL_ASSIGN',
    '/=' : 'DIV_ASSIGN',
    '%=' : 'MOD_ASSIGN',
    '&=' : 'BIT_AND_ASSIGN',
    '^=' : 'BIT_XOR_ASSIGN',
    '|=' : 'BIT_OR_ASSIGN',
    '>>' : 'RIGHT_OP',
    '<<' : 'LEFT_OP',
    '++' : 'INC_OP',
    '--' : 'DEC_OP',
    '->' : 'PTR_OP',
    '&&' : 'LOG_AND_OP',
    '||' : 'LOG_OR_OP',
    '<=' : 'LE_OP',
    '>=' : 'GE_OP',
    '==' : 'EQ_OP',
    '!=' : 'NE_OP',
    ';' : 'SEMICOLON',
    ',' : 'COMMA',
    ':' : 'COLON',
    '=' : 'EQUALS',
    '(' : 'LPAREN',
    ')' : 'RPAREN',
    '.' : 'PERIOD',
    '&' : 'BIT_AND',
    '|' : 'BIT_OR',
    '^' : 'BIT_XOR',
    '!' : 'LOG_NOT',
    '~' : 'BIT_NOT',
    '-' : 'MINUS',
    '+' : 'PLUS',
    '*' : 'TIMES',
    '/' : 'DIVIDE',
    '%' : 'MOD',
    '<' : 'LT',
    '>' : 'GT',
    '?' : 'CONDOP'
    
}

#tokens = list(reserved.values())
#tokens = tuple(reserved.values()) + (
    ## "Strings"
    #'STRING_LITERAL',
    
    ## Assignment operators
    ##..., >>=, <<=, +=
    #'ELLIPSIS', 'RIGHT_ASSIGN', 'LEFT_ASSIGN', 'ADD_ASSIGN',
    ## -=, *=, /=, %=
    #'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN',
    ## &=, ^=, |=
    #'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN'
    
    ## Standard Operators
    ## >>, <<, ++, --, ->, 
    #'RIGHT_OP', 'LEFT_OP', 'INC_OP', 'DEC_OP', 'PTR_OP',
    ## &&, ||, <=, >=, ==, !=
    #'LOG_AND_OP', 'LOG_OR_OP', 'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP',
    
    ## ;, { or <%, } or %>, ,,
    #'SEMICOLON', 'LBRACE', 'RBRACE', 'COMMA',
    ## :, =, (, ), [ or <:, ] or :>
    #'COLON', 'EQUALS', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET',
    ## ., &, !, ~, -, +
    #'PERIOD', 'BIT_AND', 'LOG_NOT', 'BIT_NOT', 'MINUS', 'PLUS',
    ## *, /, %, <, >, ^, |, ?
    #'TIMES', 'DIVIDE', 'MOD', 'LT', 'GT', 'BIT_XOR', 'BIT_OR', 'CONDOP'
#)

tokens = tuple(reserved.values()) + (
    'STRING_LITERAL',
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET'
)

# Ignore these characters
#t_ignore = ' \t\0x0C'
t_ignore = ' \t\v\n\f'

def t_error(t):
    print 'Illegal Character'
    t.lexer.skip(1)

# Check if word is a reserved value
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #t.type = reserved.get(t.value,'ID')    # Check for reserved words
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

t_STRING_LITERAL = r'[a-zA-Z0-9]?\"(\\.|[^]]"])*\"'
t_LBRACE = r'{|<%'
t_RBRACE = r'}|%>'
t_LBRACKET = r'\[|<:'
t_RBRACKET = r'\]|:>'
#ELLIPSIS = r'...'
#t_RIGHT_ASSIGN = r'>>='
#t_LEFT_ASSIGN = r'<<='
#t_ADD_ASSIGN = r'+='
#t_

#not sure how to do this yet
#t_TYPE = 

#def t_CONSTANT(t): r'co

lexer = lex.lex(debug = 0)

lexer.input(']')
while True:
    tok = lexer.token()
    if not tok:
        break
    print tok
