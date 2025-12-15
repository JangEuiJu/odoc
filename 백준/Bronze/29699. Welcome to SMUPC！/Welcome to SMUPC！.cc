#include <iostream>
#include <string>
using namespace std;


int main(void)
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    string s="WelcomeToSMUPC";
    int N;
    cin >> N; N--;
    cout << s[N % 14];
}