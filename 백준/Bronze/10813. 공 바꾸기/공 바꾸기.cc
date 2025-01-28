#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{	
	int n, m;
	int i, j;
	int temp;
	int a[100] = { 0 };

	scanf("%d %d", &n, &m);
	for (int x = 0; x < n; x++) {
		a[x] = x + 1;
	}
	for (int x = 0; x < m; x++) {
		scanf("%d %d", &i, &j);
		temp = a[i - 1];
		a[i - 1] = a[j - 1];
		a[j - 1] = temp;
	}

	for (int x = 0; x < n; x++) {
		printf("%d ", a[x]);
	}

	return 0;
}