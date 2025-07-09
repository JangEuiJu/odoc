#include <iostream>
using namespace std;
int main() {
    int k,q;
    int time = 0;
    cin >> k >> q;
    while(q--)
    {
        int t;
        char ans;
        cin >> t >> ans;
        time += t;
        if (time >= 210)
        {
            cout << k;
            break;
        }
        if (ans == 'T')
        {
            k++;
            if (k == 9) k = 1;
        }
    }
}
