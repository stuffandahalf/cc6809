#include <stdio.h>
#define TEST 5

int main (int argc, char **argv)
{
    #include "test.inc"
    //int x = 5;
    int x = TEST;
    int y = 5;
    int z = x + y;
    //printf("%d\n", z);
    return 0;
}

