D           [0-9]
L           [a-zA-Z_]

%{
#define YYSTYPE char *
#include <stdio.h>
#include <y.tab.h>
%}

void comment();
void yyerror();

%%

if              { return IF; }
while           { return WHILE; }
return          { return RETURN; }

"{"             { return OPEN_BRACE; }
"}"             { return CLOSE_BRACE; }
"("             { return '('; }
")"             { return ')'; }
"~"             { return '~'; }
"!"             { return '!'; }
"+"             { return '+'; }
"-"             { return '-'; }
"*"             { return '*'; }
"<"             { return '<'; }
"<="            { return LESS_OR_EQUAL; }
"="             { return '='; }
";"             { return ';'; }
","             { return ','; }

int             { return TYPE; }
{L}({D}|{L})*   { yylval = strdup(yytext); return IDENTIFIER; }
{D}+            { yylval = strdup(yytext); return NUMBER; }

%%

