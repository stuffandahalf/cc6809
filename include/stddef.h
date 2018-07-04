#ifndef _STDDEF_H
#define _STDDEF_H

typedef unsigned short int size_t;
typedef short int ptrdiff_t;

typedef unsigned short int wchar_t;  

#define NULL ((void *)0)

#define offsetof(TYPE, MEMBER) ((size_t)&(((TYPE *)0)->MEMBER))

#endif
