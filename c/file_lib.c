#include "lib/file_lib.h"

str read_file(str fname) {
    FILE *fp = fopen(fname, "r");
    CHECK_ERROR(fp == NULL, "File failed to open\n");
    
    int fsize = file_size(fp);
    CHECK_ERROR(!fsize, "File is empty\n");
    
    str contents = malloc(sizeof(char) * fsize);
    int index = 0;
    
    while((contents[index] = fgetc(fp)) != EOF) {
        index++;
    }
    printf("%d\n", index);
    return contents;
}

int file_size(FILE *fp) {
    fseek(fp, 0, SEEK_END);
    int fsize = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    
    return fsize;
}
