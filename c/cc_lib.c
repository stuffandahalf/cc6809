#include "lib/cc_lib.h"

Type *allocType(str key, size_t bytes) {
    Type *type = malloc(sizeof(Type));
    type->key = key;
    type->bytes = bytes;
}

void freeType(Type *type) {
    free(type);
}
