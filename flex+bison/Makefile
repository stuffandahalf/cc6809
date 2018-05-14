LEX = lex
YACC = yacc
CC = cc

cc: lex.yy.c y.tab.c
	$(CC) -o $@ lex.yy.c y.tab.c
	
lex.yy.c: cc6809.l
	$(LEX) $<

y.tab.c: cc6809.y
	$(YACC) -d $<

clean: 
	rm -f cc
	rm -f lex.yy.c
	rm -f y.tab.c
	rm -f y.tab.h
