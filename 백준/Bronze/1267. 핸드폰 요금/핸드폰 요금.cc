#include <iostream>
using namespace std;

int main(void)
{
    int N, Y = 0, M = 0;
    cin >> N;
    
    for (int i = 0; i < N; i++)
    {
        int T;
        cin >> T;
        Y += (T / 30 + 1) * 10;
        M += (T / 60 + 1) * 15;
    }
    
    if (Y == M)
        cout << "Y M " << Y << "\n";
    else if (Y > M)
        cout << "M " << M << "\n";
    else
        cout << "Y " << Y << "\n";


}