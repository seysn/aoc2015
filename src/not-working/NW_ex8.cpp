#include <iostream>
#include <fstream>
#include <ctype.h>

using namespace std;

int main(int argc, char const *argv[]) {
    ifstream file("input8.txt");
    int tmpi, tmpj;
    int res_char = 0, res_tot = 0, cpt = 0;
    string s;

    while (file >> s) {
        tmpi = res_char;
        tmpj = res_tot;
        for (size_t i = 0; i < s.size(); i++) {
            switch (s[i]) {
                case '\"':
                    break;
                case '\\':
                    res_tot++;
                    i++;
                    if (s[i] == 'x') {
                        if (s[i + 1] == '\\' && s[i + 2] == '\\') {
                            if (s[i + 3] == '\\' && s[i + 4] == '\\') {
                                i += 4;
                                res_tot += 4;
                            } else {
                                i += 3;
                                res_tot += 3;
                            }
                        } else if (s[i + 2] == '\\' && s[i + 3] == '\\') {
                            i += 3;
                            res_tot += 3;
                        } else {
                            i += 2;
                            res_tot += 2;
                        }
                        res_char++;
                    } else if (s[i] == '\"') {
                        // res_tot++;
                        res_char++;
                    }
                    break;
                default:
                    res_char++;
                    break;
            }
            res_tot++;
        }
        cout << s << " char:" << res_char - tmpi << " tot:" << res_tot - tmpj << endl;
        cpt++;
    }
    
    cout << res_tot - res_char << endl;

    return 0;
}
