#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable: 4996)
#include <iostream>
#define endl '\n'
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);   cout.tie(NULL);
    
    int a, e;
    cin >> a >> e;
    
    if (a >= 3 && e <= 4) {
        cout << "TroyMartian" << endl;
    }
    if (a <= 6 && e >= 2) {
        cout << "VladSaturnian" << endl;
    }
    if (a <= 2 && e <= 3) {
        cout << "GraemeMercurian" << endl;
    }
}
