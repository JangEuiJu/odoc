#include <iostream>
#include <string>

using namespace std;

int n;
string m;
bool p[100][100];
bool h[100][100]; 
int row, col; 

bool isValidLocation(const int& row, const int& col) {
	if (row < 0 || row >= n || col < 0 || col >= n) 
		return false;
	
	return true;
}

int main() {
	cin >> n;
	cin >> m;

	for (int i = 0; i < m.size(); i++) {
		if (m[i] == 'U') {
			if (!isValidLocation(row - 1, col)) continue;

			p[row][col] = true;
			p[--row][col] = true;
		}
		else if (m[i] == 'D') {
			if (!isValidLocation(row + 1, col)) continue;

			p[row][col] = true;
			p[++row][col] = true;
		}
		else if (m[i] == 'L') {
			if (!isValidLocation(row, col - 1)) continue;

			h[row][col] = true;
			h[row][--col] = true;
		}
		else {
			if (!isValidLocation(row, col + 1)) continue;

			h[row][col] = true;
			h[row][++col] = true;
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (p[i][j] && h[i][j]) printf("+");
			else if (p[i][j]) printf("|");
			else if (h[i][j]) printf("-");
			else printf(".");
		}

		printf("\n");
	}

	return 0;
}