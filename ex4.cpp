#include <iostream>
#include <stdio.h>
#include "md5.h" // Need to compile md5.cpp to execute the program

using namespace std;

string concatenate(string s, int i) {
    char numstr[21];
    sprintf(numstr, "%d", i);
    string res(s + numstr);
    return res;
}

int main(int argc, char const *argv[]) {
    string input("bgvyzdsv"), output(md5(input));
    int cpt(1);

    while (1) {
        output = md5(concatenate(input, cpt));
        if (output.substr(0, 5) == "00000") {
            cout << "Trouvé : " << cpt << endl;
            break;
        }
        cpt++;
    }

    cout << "The answer is " << cpt << endl;

    return 0;
}
