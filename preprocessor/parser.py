# -*- coding: utf-8 -*-

import ply.lex as lex
import ply.yacc as yacc

class Parser:
    """
    Base class for a lexer/parser that has rules defined as methods
    """
    literals = ()
    tokens = ()
    precedence = ()
    
    def __init__(self, **kw):
        self.debug = kw.get('debug', 0)
        self.names = {}
        #try:
        #    modname = os.path.split(os.path.splitext(__file__)[0])[
        #        1] + "_" + self.__class__.__name__
        #except:
        #    modname = "parser" + "_" + self.__class__.__name__
        #self.debugfile = modname + ".dbg"
        #self.tabmodule = modname + "_" + "parsetab"
        # print self.debugfile, self.tabmodule

        # Build the lexer and parser
        #lex.lex(module=self, debug=self.debug)
        #yacc.yacc(module=self,
        #          debug=self.debug,
        #          debugfile=self.debugfile,
        #          tabmodule=self.tabmodule)
        lex.lex(module = self, debug = 0)
        yacc.yacc(module = self)

    # def run(self):
        # while 1:
            # try:
                # s = raw_input('calc > ')
            # except EOFError:
                # break
            # if not s:
                # continue
            # yacc.parse(s)
    
    def parse(self, data, debug = 0):
        yacc.error = 0
        p = yacc.parse(data, debug = debug)
        if yacc.error:
            return None
        return p
