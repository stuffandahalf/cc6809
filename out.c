# 1 "test_files/test2.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 1 "<command-line>" 2
# 1 "test_files/test2.c"
# 1 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h" 1 3 4
# 149 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h" 3 4

# 149 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h" 3 4
typedef long int ptrdiff_t;
# 216 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h" 3 4
typedef long unsigned int size_t;
# 328 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h" 3 4
typedef int wchar_t;
# 426 "/usr/lib/gcc/x86_64-linux-gnu/5/include/stddef.h" 3 4
typedef struct {
  long long __max_align_ll __attribute__((__aligned__(__alignof__(long long))));
  long double __max_align_ld __attribute__((__aligned__(__alignof__(long double))));
} max_align_t;
# 2 "test_files/test2.c" 2



# 4 "test_files/test2.c"
int main (int argc, char **argv)
{
    __uint8_t s = 5;
    int x = 5;
    int y = 5;
# 1 "test_files/test2.inc" 1
int z = x + y;
# 10 "test_files/test2.c" 2
    return z;
}
