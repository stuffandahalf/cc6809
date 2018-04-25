#include <iostream>
#include <fstream>
//#include <cstdio>
//#include <cstdlib>

int main(int argc, char **argv)
{
    using namespace std;
	if (argc < 2) {
        //cerr << "Insufficient arguments" << endl;
        cerr << "Syntax:\n./cc6809 fname.c" << endl;
        return 1;
    }
    
    /*FILE *cfile = fopen(argv[1], "r");
    fseek(cfile, 0, SEEK_END);
    int fsize = ftell(cfile);
    fseek(cfile, 0, SEEK_SET);
    
    cout << fsize << endl;*/
    
    ifstream cfile;
    cfile.open(argv[1]);
    if (!cfile.is_open()) {
        cerr << "File failed to open." << endl;
        return 1;
    }
    
    
	return 0;
}

