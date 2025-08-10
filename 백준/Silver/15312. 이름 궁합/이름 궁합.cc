#include <iostream>
#include <vector>
#include <string>
using namespace std;

int line[26] = { 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 };

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    string a, b;
    cin >> a >> b;

    vector<int>combine;
    for (int i = 0; i < a.size(); i++) {
        combine.push_back(line[a[i] - 'A']);
        combine.push_back(line[b[i] - 'A']);
    }

    while (1) {
        vector<int>tmp;
        for (int i = 0; i < combine.size() - 1; i++)
            tmp.push_back((combine[i] + combine[i + 1]) % 10);

        combine = tmp;
        if (combine.size() == 2) {
            cout << combine[0] << combine[1] << '\n';
            return 0;
        }
    }
}