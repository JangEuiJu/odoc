#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n; cin >> n;

  for (int c = 0; c < n; c++) {
    string bits; cin >> bits;

    int cntErr = 0;
    for (size_t i = 0; i < bits.size(); i += 8) {
      int cntOnes = 0;
      for (int j = 0; j < 7; j++)
        if (bits[i + j] == '1')
          cntOnes++;
      if ((cntOnes % 2) != (bits[i + 7] - '0'))
        cntErr++;
    }
    cout << cntErr << "\n";
  }

  return 0;
}