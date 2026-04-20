#include<iostream>
#include<algorithm>
using namespace std;
int t[101], vi[101];

int main()
{
	int n, a, b, answer=0, c, solve;
	scanf("%d %d %d", &n, &a, &b);
	for (int i = 1; i <= n; i++)scanf("%d", &t[i]);
	sort(t + 1, t + n + 1);
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= 100; j++)vi[j] = 0;
		if (i != 0) {
			c = 0; solve = 0;
			for (int j = 1; j <= n; j++) {
				if (solve == i)break;
				if (t[j] >= c + a) {
					solve++;
					c += a;
					vi[j] = 1;
				}
			}
			if (solve != i)break;
		}
		else {
			c = 0;
			solve = 0;
		}
		for (int x = 0; x < a; x++){
			int cc = b * x + c, after_solve = 0, nA = a - x;
			for (int j = 1; j <= n; j++) {
				if (cc + nA <= t[j] && vi[j] == 0) {
					after_solve++;
					cc += nA;
				}
			}

			if (solve + after_solve > answer)answer = solve + after_solve;
		}
	}
	printf("%d\n", answer);
	return 0;
}