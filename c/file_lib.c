#include "lib/file_lib.h"

String *read_file(str fname) {
    FILE *fp = fopen(fname, "r");
    CHECK_ERROR(fp == NULL, "File failed to open\n");
    
    size_t fsize = file_size(fp);
    CHECK_ERROR(!fsize, "File is empty\n");
    
    String *string = allocString(fsize);
    
    for (int i = 0; i < fsize; i++) {
        string->contents[i] = fgetc(fp);
    }
    
    return string;
}

size_t file_size(FILE *fp) {
    fseek(fp, 0, SEEK_END);
    size_t fsize = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    
    return fsize - 1;   //ignore EOF
}

/*
str *split_str(str string, char delim) {
    int count = 0;
    while(
}*/
