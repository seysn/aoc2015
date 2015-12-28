#include <iostream>
#include <fstream>
#include <ctype.h>

using namespace std;

int main(int argc, char const *argv[]) {
    ifstream file("inputs/input8.txt");
    int res_char = 0, res_tot = 0, cpt = 0;
    string s;

    while (file >> s) {
        res_tot += s.size();

        for (size_t i = 1; i < s.size() - 1;) {
            res_char++;
            if (s[i] == '\\') {
                if (s[i + 1] == 'x')
                    i += 4;
                else
                    i += 2;
            } else {
                i++;
            }
        }
    }

    cout << res_tot - res_char << endl;

    return 0;
}
