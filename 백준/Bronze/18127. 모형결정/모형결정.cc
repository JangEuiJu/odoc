#pragma GCC target("avx,avx2,fma")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
#define int int64_t
using namespace std;

int32_t main(){
  fastio;
  int a,b,ret = 0,temp = 1; cin >> a >> b;
  for(int i = 0; i <= b; i++){
    ret += temp;
    temp += a - 2;
  }
  cout << ret << "\n";
}