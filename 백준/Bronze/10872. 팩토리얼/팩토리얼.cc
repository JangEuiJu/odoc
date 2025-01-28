#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

int factorial(int n) {
	if (n == 0)
		return 1;
	else
		return n * factorial(n - 1);
}

int main() {

	int n;
	scanf("%d", &n);
	printf("%d", factorial(n));
	
	return 0;
}
