#include <iostream>

using namespace std;

long long T, N;

void binarySearch() {
  unsigned long long left = 1;
  unsigned long long right = N;
  unsigned long long mid;

  while (left <= right) {
    mid = (left + right) / 2;

    if (mid * (mid + 1) / 2 <= N) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  cout << right << '\n';
}

void solve() {
  cin >> T;

  while (T--) {
    cin >> N;

    binarySearch();
  }
}

int main() {
  solve();
}