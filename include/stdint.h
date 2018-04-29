#ifndef _STDINT_H
#define _STDINT_H

typedef signed char int8_t;
typedef unsigned char uint8_t;

typedef signed int int16_t;
typedef unsigned int uint16_t;

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
