#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[]) {
    ifstream file("inputs/input6.txt");
    string line;

    while ((line = getline(file, line)) == )
    size_t pos = 0;
    string token;
    while ((pos = s.find(' ')) != string::npos) {
        token = s.substr(0, pos);
        cout << token << endl;
        s.erase(0, pos + 1);
    }

    return 0;
}
