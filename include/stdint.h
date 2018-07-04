#ifndef _STDINT_H
#define _STDINT_H

/*#if BITS == 8
#include <8bit/types.h>
#endif

typedef __int8_t int8_t;
typedef __uint8_t uint8_t;

typedef __int16_t int16_t;
typedef __uint16_t uint16_t;

typedef __int32_t int32_t;
typedef __uint32_t uint32_t;

typedef __int64_t int64_t;
typedef __uint64_t uint64_t;*/

typedef signed char int8_t;
typedef unsigned char uint8_t;

typedef signed short int int16_t;
typedef unsigned short int uint16_t;

typedef signed long int int32_t;
typedef unsigned long int uint32_t;

typedef signed long long int int64_t;
typedef unsigned long long int uint64_t;

#define INT8_MAX 127
#define INT8_MIN -128
#define UINT8_MAX 255

#define INT16_MAX 32767
#define INT16_MIN -32768
#define UINT16_MAX 65535

#define INT32_MAX 2147483647
#define INT32_MIN -2147483648
#define UINT32_MAX 4294967295

#define INT64_MAX 9223372036854775807
#define INT64_MIN -9223372036854775808
#define UINT64_MAX 18446744073709551615

#endif
