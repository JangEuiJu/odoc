#include <stdio.h>

int main(void)
{
	int n;
	int a[100];
	int v;
	int cnt = 0;

	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	
	scanf("%d", &v);

	for (int i = 0; i < n; i++) {
		if (a[i] == v)
			cnt++;
	}

	printf("%d", cnt);

	return 0;
}