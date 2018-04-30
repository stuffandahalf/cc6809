# -*- coding: utf-8 -*-

# Equivalent YACC
# assign  : NAME EQUALS expr
# expr    : expr PLUS term
        # | expr MINUS term
        # | term
# term    : term TIMES factor
        # | term DIVIDE factor
        # | factor
# factor  : NUMBER

import ply.yacc as yacc
import cclex

tokens = cclex.tokens

# precedence = (
    # ('left', 'PLUS', 'MINUS'),
    # ('left', 'TIMES', 'DIVIDE')
# )

def p_assign(p):
    '''assign : NAME EQUALS expr'''

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''

def p_factor(p):
    '''factor : NUMBER'''

ccparser = yacc.yacc()

def parse(data, debug=0):
    ccparser.error = 0
    p = ccparser.parse(data, debug=debug)
    if ccparser.error:
        return None
    return p
#ast = ccparser.parse(cclex.str)
#print ast
