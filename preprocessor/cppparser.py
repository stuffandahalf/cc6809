# -*- coding: utf-8 -*-

from parser import Parser

class CPP(Parser):
    literals = ()
    tokens = (
        #'NEWLINE',
        # #, <, >, "
        'POUND', 'LIBL', 'LIBR', 'QUOTE',
        'COMMENTL', 'COMMENTR', 'COMMENT',
        'INCLUDE', 'IFDEF', 'IFNDEF', 'ELSE', 'ENDIF',
        'DEFINE', 'ID', 'VALUE',
        'LOCFILE', 'LIBFILE',
        'FNAME'
    )
    
    #precedence = (
    #    ('nonassoc', 'INCLUDE', 'DEFINE')
    #)
    
    # Ignore most whitespace characters
    t_ignore = ' \t'
    
    #t_NEWLINE = '\n'
    
    # Tokens for preprocessing
    t_POUND = r'\#'
    t_LIBL = r'\<'
    t_LIBR = r'\>'
    t_QUOTE = r'\"'
    
    t_COMMENTL = '/\*'
    t_COMMENTR = '\*/'
    t_COMMENT = '//'
    
    # Preprocessor directives
    t_INCLUDE = r'include'
    t_IFDEF = r'ifdef'
    t_IFNDEF = r'ifndef'
    t_ELSE = r'else'
    t_ENDIF = r'endif'
    t_DEFINE = r'define'
    t_ID = r'[A-Za-z_][A-Za-z0-9_]*'
    t_VALUE = r'.+'

    # Filetypes for includes
    #t_FNAME = r'\"[^\#\<\>\"]+'
    t_LOCFILE = r'\"[^\#\<\>\"]+\"'
    t_LIBFILE = r'\<[^\#\<\>\"]+\>'
    
    def t_error(self, t):
        print "Illegal character %s" % t.value[0]
        t.lexer.skip(1)
    
    # YACC rules
    #def p_comment(self, p):
        #'''comment : COMMENT VALUE* NEWLINE'''
    
    def p_include(self, p):
        '''include : include_directive include_file'''
        
    def p_include_directive(self, p):
        '''include_directive : POUND INCLUDE'''

    def p_include_file(self, p):
        '''include_file : LOCFILE
                        | LIBFILE'''

    def p_define(self, p):
        '''define : POUND DEFINE ID
                  | POUND DEFINE ID VALUE'''

    # def p_ifdef(self, p):
        # '''ifdef : POUND IFDEF ID'''
