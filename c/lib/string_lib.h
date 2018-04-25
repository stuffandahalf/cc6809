#ifndef STRING_LIB_H
#define STRING_LIB_H

#include <stdlib.h>
#include <string.h>

typedef char * str;

typedef struct {
    int length;
    str contents;
} String;

String *allocString(size_t length);
void freeString(String *string);

#endif
