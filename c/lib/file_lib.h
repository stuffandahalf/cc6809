#ifndef FILE_LIB_H
#define FILE_LIB_H

#include <stdio.h>
#include <stdlib.h>

#include "cc_lib.h"

str read_file(str fname);
int file_size(FILE *fp);

#endif
