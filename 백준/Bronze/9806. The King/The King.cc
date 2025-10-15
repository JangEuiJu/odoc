#include <bits/stdc++.h>

using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, P;
    cin >> N >> P;

    int answer = 0;

    for (int i = 0; i < N; i++) {
        int M;
        cin >> M;

        int X = 1;
        for (int p = 0; p < P; p++) X *= M;
        if (X > 0) answer += X;
    }

    cout << answer << endl;
}