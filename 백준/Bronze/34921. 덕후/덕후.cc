#include <iostream>

using namespace std;

int A, T;

int main()
{
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> A >> T;
    cout << max((10 + 2 * (25 - A + T)), 0);
    return 0;
}