#ifndef FILE_LIB_H
#define FILE_LIB_H

#include <stdio.h>
#include <stdlib.h>

#include "string_lib.h"
#include "cc_lib.h"

String *read_file(str fname);
size_t file_size(FILE *fp);
//str *split_str(str string, char delim);

#endif
