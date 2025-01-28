#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		for (int j = 1; j < n - i; j++) {
			printf(" ");
		}
		for (int j = 0; j < (i+1)*2-1; j++) {
			printf("*");
		}
		printf("\n");
	}

	for (int i = n-1; i > 0; i--) {
		for (int j = n - i; j > 0; j--) {
			printf(" ");
		}
		for (int j = 0; j < 2 * i - 1; j++) {
			printf("*");
		}
		printf("\n");
	}


	return 0;
}