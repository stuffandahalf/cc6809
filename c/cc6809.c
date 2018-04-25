#include <stdio.h>
#include <stdlib.h>

#include "lib/cc_lib.h"
#include "lib/file_lib.h"

int main(int argc, char **argv)
{
    CHECK_ERROR(argc < 2, "Syntax:\n./cc6809 fname.c\n");
    
    FILE *cfile = fopen(argv[1], "r");
    CHECK_ERROR(cfile == NULL, "File failed to open\n");
    fseek(cfile, 0, SEEK_END);
    int fsize = ftell(cfile);
    CHECK_ERROR(!fsize, "File is empty\n");
    fseek(cfile, 0, SEEK_SET);
    
    printf("%d\n", fsize);
    
    //str buffer[fsize];
    str buffer = malloc(sizeof(char) * fsize);
    int index = 0;
    
    while((buffer[index] = fgetc(cfile)) != EOF) {
        index++;
    }
    
    printf("%s", buffer);
    
    fclose(cfile);
    
    free(buffer);
	return 0;
}

