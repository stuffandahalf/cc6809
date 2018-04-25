#define MC6809
//#define MC68K
//#define Z80
//#define MOS6502

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "lib/cc_lib.h"
#include "lib/string_lib.h"
#include "lib/file_lib.h"

//char, int, 

//Type types[10] = 

int main(int argc, char **argv)
{
    CHECK_ERROR(argc < 2, "Syntax:\n./cc6809 fname.c\n");
    //str code = read_file(argv[1]);
    String *code = read_file(argv[1]);
    //strtok(code, "\n");
    printf("%s\n", code->contents);
    
    freeString(code);
	return 0;
}

