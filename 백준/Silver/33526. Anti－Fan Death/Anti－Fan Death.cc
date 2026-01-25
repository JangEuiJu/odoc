#include <iostream>
using namespace std;

int N;
char A[3][3] = {{'Z','N','A'},{'N','A','Z'},{'A','Z','N'}};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int r = 0; r < 3; r++) {
        for (int p = 0; p < N; p++) {
            for (int c = 0; c < 3; c++) {
                for (int k = 0; k < N; k++) cout << A[r][c];
            }
            cout << '\n';
        }
    }
}