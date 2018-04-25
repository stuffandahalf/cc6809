#ifndef STDIO_H
#define STDIO_H

#include "stdlib.h"

int fprintf(FILE *__stream, const char *__format, ...);
int printf(const char *__format, ...);

int fscanf(FILE *__stream, const char *__format, ...);
int scanf(const char *__format, ...);

#endif
