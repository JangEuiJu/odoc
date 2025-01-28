#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std; 
string a;
int n;
 
int main()
{
    ios::sync_with_stdio(false); 
    cin.tie(nullptr); cout.tie(nullptr);// 입출력 시간 단축
    
    cin >> n;
    while (n--) {
        cin >> a;
        cout << a.size() << '\n';
    }
    return 0;
}
 