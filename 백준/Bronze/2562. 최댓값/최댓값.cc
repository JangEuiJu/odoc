#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int max = 0;
	int count;
	int a[9];
	for (int i = 0; i < 9; i++) {
		scanf("%d", &a[i]);
		if (a[i] > max) {
			max = a[i];
			count = i + 1;
		}
	}
	printf("%d\n%d", max, count);
	

	return 0;
}