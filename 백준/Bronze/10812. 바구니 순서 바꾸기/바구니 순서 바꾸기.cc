#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int n, m, i, j, begin, end, mid, t;
	int a[100];
	int temp[100];
	
	scanf("%d %d", &n, &m);
	for (int i = 0; i < 100; i++)
		a[i] = i + 1;
	for (int i = 0; i < m; i++) {
		scanf("%d %d %d", &begin, &end, &mid);
		for (int j = 0; j < end - begin + 1; j++) {
			t = mid + j;
			if (t > end)
				temp[j] = a[t - end - 2 + begin];
			else
				temp[j] = a[t - 1];
		}
		for (int j = 0; j < end - begin + 1; j++) {
			a[j + begin - 1] = temp[j];
		}
	}
	for (int i = 0; i < n; i++) {
		printf("%d ", a[i]);
	}
	printf("\n");



	return 0;
}