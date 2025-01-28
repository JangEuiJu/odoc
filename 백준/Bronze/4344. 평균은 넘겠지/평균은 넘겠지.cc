#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>


int main(){
	int c, n;
	int arr[1000];
	int sum = 0, count = 0;
	int average = 0;
	scanf("%d", &c);

	for (int i = 0; i < c; i++) {
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
			scanf("%d", &arr[j]);
		for (int k = 0; k < n; k++)
			sum += arr[k];
		average = sum / n;
		for (int x = 0; x < n; x++)
			if (arr[x] > average)
				count++;
		printf("%.3f%%\n", (double)count / n * 100);
		average = 0; sum = 0;  count = 0;
	}

	return 0;
}