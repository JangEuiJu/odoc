#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

	int a[6] = { 1, 1, 2, 2, 2, 8 };
	int b[6] = { 0 };
	for (int i = 0; i < 6; i++) {
		scanf("%d", &b[i]);
	}
	for (int i = 0; i < 6; i++) {
		printf("%d ", a[i]-b[i]);
	}

	return 0;
}