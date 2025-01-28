#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a[100] = {0};
	int n, m, i, j, k;
	scanf("%d %d", &n, &m);

	for (int x = 0; x < m; x++) {
		scanf("%d %d %d", &i, &j, &k);
		for (int y = i; y <= j; y++) {
			a[y] = k;
		}
	}
	for (int x = 1; x <= n; x++) {
		printf("%d ", a[x]);
	}

	return 0;
}