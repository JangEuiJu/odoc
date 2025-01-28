#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;

  int maxArea = 0;
  for (int i = 0; i < n; i++) {
    int h, w; cin >> h >> w;
    maxArea = max(maxArea, h * w);
  }

  cout << maxArea << "\n";

  return 0;
}