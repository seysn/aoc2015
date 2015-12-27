#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[]) {
    ifstream file("inputs/input1.txt");
    int cpt = 0, i = 0;
    char c;

    while (file >> c) {
        if (c == '(')
            cpt++;
        else
            cpt--;
        i++;

        if (cpt == -1)
            break;
    }

    cout << "Position : " << i << endl;

    return 0;
}
