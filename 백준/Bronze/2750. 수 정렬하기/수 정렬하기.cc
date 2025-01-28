#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

void sort(int* arr, int n) {
	int i, j;
	int min, temp;
	for (i = 0; i < n; i++) {
		min = arr[i];
		for (j = i+1; j < n; j++) {
			if (arr[j] < min) {
				min = arr[j];
				temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}		
		}
	}
}

int main(){
	int n;
	int* arr;
	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int) * n);

	if (arr != NULL) {
		for (int i = 0; i < n; i++)
			scanf("%d", &arr[i]);
		sort(arr, n);
		for (int i = 0; i < n; i++)
			printf("%d\n", arr[i]);
	}
	
	
	free(arr);

	return 0;
}