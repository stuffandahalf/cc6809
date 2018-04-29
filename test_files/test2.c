#include <stdio.h>
#define TEST 5

int main (int argc, char **argv)
{
    #include "test.inc"
    //int x = 5;
    int x = TEST;
    int y = 5;
    int z = x + y;
    //printf("%d\n", x);
    //printf("%d\n", z);
    //printf("%p\n", (void *)0);
    //printf("%p\n", NULL);
    return 0;
}

