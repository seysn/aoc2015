#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char const *argv[]) {
    ifstream file("input2.txt");
    int l, w, h, smallest, res = 0;
    char dump;

    while (file >> l >> dump >> w >> dump >> h) {
        smallest = l * w;
        if (w * h < smallest) smallest = w * h;
        if (h * l < smallest) smallest = h * l;

        res += smallest + (2 * l * w) + (2 * w * h) + (2 * h * l);
    }

    cout << "Le total est : " << res << endl;

    return 0;
}
