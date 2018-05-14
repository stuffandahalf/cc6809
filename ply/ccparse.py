# Written by Gregory Norton
# Based from https://github.com/dabeaz/ply/blob/master/example/ansic/cparse.py

# -*- coding: utf-8 -*-

import ply.yacc as yacc
import cclex

tokens = cclex.tokens

# precedence = (
    # ('left', 'PLUS', 'MINUS'),
    # ('left', 'TIMES', 'DIVIDE')
# )

def p_assign(p):
    '''assign : ID EQUALS expr'''
    #'''assign : TYPEID ID EQUALS expr'''
    #print len(p)
    #print p.__dict__

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term MOD factor
            | factor'''

def p_factor(p):
    '''factor : ICONST'''

ccparser = yacc.yacc()

def parse(data, debug=0):
    ccparser.error = 0
    p = ccparser.parse(data, debug=debug)
    if ccparser.error:
        return None
    return p
    
#ast = ccparser.parse(cclex.str)
#print ast
