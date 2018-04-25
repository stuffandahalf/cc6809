#ifndef CC_LIB_H
#define CC_LIB_H

#include <stdlib.h>

#include "string_lib.h"

#define CHECK_ERROR(cond, msg) {\
    if ((cond)) {\
        fprintf(stderr, (msg));\
        exit(1);\
    }\
}

typedef struct {
    str key;
    size_t bytes;
} Type;

Type *allocType(str key, size_t bytes);
void freeType(Type *type);

#define TYPES 7

#if defined(MC6809) || defined(MOS6502) || defined(Z80)
const Type types[TYPES] = {
    { .key = "*", .bytes = 2 },
    { .key = "void", .bytes = 0 },
    { .key = "char", .bytes = 1 },
    { .key = "byte", .bytes = 1 },
    { .key = "short", .bytes = 2 },
    { .key = "int", .bytes = 2 },
    { .key = "long", .bytes = 4 }
};
    
#elif defined(MC68K)
const Type types[TYPES] = {
    { .key = "*", .bytes = 4 },
    { .key = "void", .bytes = 0 },
    { .key = "char", .bytes = 1 },
    { .key = "byte", .bytes = 1 },
    { .key = "short", .bytes = 2 },
    { .key = "int", .bytes = 4 },
    { .key = "long", .bytes = 8 }
};

#endif

Type **primatives();

#endif
