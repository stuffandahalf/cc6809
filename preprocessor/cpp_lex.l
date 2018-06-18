/*
Gregory Norton
June 17 2018
*/

D           [0-9]
L           [a-zA-Z_]

%{
#include <stdio.h>
#include "y.tab.h"
%}

void comment();
void yyerror();

%%

"#"         { return POUND; }
"//"[^\n]*  { /* Discard preprocessor comments. */}
"/*"        { comment(); }
[ \t\n]+    { /* Ignore whitespace */ }

"{"         { return OPEN_BRACE; }
"}"         { return CLOSE_BRACE; }
"("         { return '('; }
")"         { return ')'; }
","         { return ','; }

"\\"        { return '\'}

{L}({L}|{D})*   { yylval = strdup(yytext); return IDENTIFIER; }

%%

void comment() {
    /* Consume character up to the closing comment marker. */
    char c, prev = 0;

    while ((c = input()) != INPUT_EOF) {
        if (c == '/' && prev == '*') {
            return;
        }
        prev = c;
    }
    yyerror("unterminated comment");
}
