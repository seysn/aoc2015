#include <utility>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[]) {
    ifstream file("inputs/input3.txt");
    int xy[2] = {0, 0};
    char c;

    vector<pair<int, int> > liste;
    liste.push_back(make_pair(xy[0], xy[1]));

    while (file >> c) {
        switch (c) {
            case '^':
                xy[0]++;
                break;
            case 'v':
                xy[0]--;
                break;
            case '<':
                xy[1]--;
                break;
            case '>':
                xy[1]++;
                break;
        }

        if (find(liste.begin(), liste.end(), make_pair(xy[0], xy[1])) == liste.end()) {
            liste.push_back(make_pair(xy[0], xy[1]));
        }
    }

    cout << "Le nombre de maison distribuées : " << liste.size() << endl;

    return 0;
}
