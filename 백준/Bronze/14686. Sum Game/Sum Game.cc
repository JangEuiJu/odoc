#include <iostream>
using std::cin;
using std::cout;
int games[100000];

int main()
{
    std::ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    for (int i = 0;i < N;i++) { 
        int x;
        cin >> x;
        if (i == 0) games[i] = x;
        else games[i] = games[i - 1] + x;
    }
    int prefixsum = 0;
    int ans = 0;
    for (int i = 0;i < N;i++) {
        int x;
        cin >> x;
        prefixsum += x;
        if (prefixsum == games[i]) ans = i + 1; 
    }
    cout << ans;

    return 0;
}