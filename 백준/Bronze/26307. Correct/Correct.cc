#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int hh, mm; cin >> hh >> mm;

  int startTime = 9 * 60,
      submitTime = hh * 60 + mm;

  int timeConsumed = submitTime - startTime;

  cout << timeConsumed << "\n";

  return 0;
}