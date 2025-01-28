#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b) {
	return (*(int*)a - *(int*)b); 
}

int search(int arr[], int N, int T) {
	int low = 0;
	int high = N - 1;
	int mid;

	while (low <= high) {
		mid = (low + high) / 2;

		if (arr[mid] == T)
			return 1;
		else if (arr[mid] > T)
			high = mid - 1;
		else
			low = mid + 1;
	}

	return 0;
}

int main(void) {
	int N, M, T;
	
	scanf("%d", &N);
	int* arr = (int*)malloc(sizeof(int) * N);

	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	qsort(arr, N, sizeof(int), compare);
	
	scanf("%d", &M);
	for (int i = 0; i < M; i++) {
		scanf("%d", &T);
		printf("%d ", search(arr, N, T));
	}
		

	free(arr);
	return 0;
}