#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int getSmallest(vector<int> &v) {
    int small_id = 0;

    for (int i = 1; i < v.size(); i++) {
        if (v[small_id] > v[i]) {
            small_id = i;
        }
    }

    int res = v[small_id];
    v.erase(v.begin() + small_id);
    return res;
}

int main(int argc, char const *argv[]) {
    ifstream file("inputs/input2.txt");
    int l, w, h, smallest, secsmallest, res = 0;
    char dump;
    vector<int> list;

    while (file >> l >> dump >> w >> dump >> h) {
        list.push_back(l);
        list.push_back(w);
        list.push_back(h);

        smallest = getSmallest(list);
        secsmallest = getSmallest(list);

        cout << "l:" << l << " w:" << w << " h:" << h << " small:" << smallest << " 2small:" << secsmallest << " res:" << (smallest * 2) + (secsmallest * 2) + (l * w * h) << endl;

        res += (smallest * 2) + (secsmallest * 2) + (l * w * h);
        list.clear();
    }

    cout << "Le total est : " << res << endl; // Not 5766194 && 3833824

    return 0;
}
