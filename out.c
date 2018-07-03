# 1 "test_files/test2.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 31 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 32 "<command-line>" 2
# 1 "test_files/test2.c"
# 1 "include/stdio.h" 1



# 1 "include/stddef.h" 1



typedef uint16_t size_t;
# 5 "include/stdio.h" 2



int fprintf(FILE *__stream, const char *__format, ...);
int printf(const char *__format, ...);

int fscanf(FILE *__stream, const char *__format, ...);
int scanf(const char *__format, ...);
# 2 "test_files/test2.c" 2


int main (int argc, char **argv)
{
# 1 "test_files/test2.inc" 1
printf("hello test\n");
# 7 "test_files/test2.c" 2

    int x = 5;
    int y = 5;
    int z = x + y;




    return 0;
}
