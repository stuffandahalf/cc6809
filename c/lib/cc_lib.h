#ifndef CC_LIB_H
#define CC_LIB_H

typedef char * str;

#define CHECK_ERROR(cond, msg) {\
    if ((cond)) {\
        fprintf(stderr, (msg));\
        exit(1);\
    }\
}

#endif
