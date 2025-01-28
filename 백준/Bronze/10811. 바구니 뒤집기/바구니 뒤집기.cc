#include <stdio.h>
#include <stdlib.h>

int main()
{	
	int a[100] = { 0 };
	int n, m, x, y;
	int temp;
	
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		a[i] = i + 1;
	}

	for (int i = 0; i < m; i++) {
		scanf("%d %d", &x, &y);
		for (int j = x-1; j <= y-1; j++, y--) {
			temp = a[j];
			a[j] = a[y-1];
			a[y-1] = temp;
		}
	}
	

	for (int i = 0; i < n; i++) {
		printf("%d ", a[i]);
	}
	
	return 0;
}