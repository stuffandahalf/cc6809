#include "lib/string_lib.h"

String *allocString(size_t length) {
    String *string = malloc(sizeof(String));
    string->contents = malloc(sizeof(char) * length);
    string->length = length;
    
    return string;
}

void freeString(String *string) {
    free(string->contents);
    free(string);
}
