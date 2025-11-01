#include <iostream>
#include <string>
using namespace std;

string s;
int main() {
	int n;
	cin >> n;
	cin >> s;
	int w = 0, state = 0;
	for (int i = 0; s[i]; i++) {
		if (s[i] == 'W') {
			if (++w == 2) {
				if (state == 0) cout << 5;
				else if(state == 1) cout << 1;
				else cout << 6;
				return 0;
			}
			
		}
		else if (s[i] == 'P') {
			if(state < 2) state ^= 1;
			if (w == 1) {
				state = 2;
			}
		}
	}
	cout << 0;
}