#include <iostream>
#include <vector>
using namespace std;
#define MAX_NUMBER 318137
vector<bool> isNotPrime;
vector<int> primes;
int T, n;
int main()
{
    ios::sync_with_stdio(0), cin.tie(0);

    isNotPrime = vector<bool>(MAX_NUMBER + 1);
    isNotPrime[1] = true;

    for (int i = 2; i * i <= MAX_NUMBER; ++i)
    {
        if (!isNotPrime[i])
        {
            for (int j = i * i; j <= MAX_NUMBER; j += i)
            {
                isNotPrime[j] = true;
            }
        }
    }

    for (int i = 2, j = 0; i <= MAX_NUMBER; ++i)
    {
        if (!isNotPrime[i]) 
        {
            ++j;
            if (!isNotPrime[j]) 
            {
                primes.push_back(i);
            }
        }
    }

    cin >> T;
    while (T--)
    {
        cin >> n;
        cout << primes[--n] << "\n";
    }
}