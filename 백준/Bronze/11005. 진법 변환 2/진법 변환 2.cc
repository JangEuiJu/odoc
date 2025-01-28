#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

void binary(int N, int B) {
	if (N != 0) {
		binary(N / B, B);
		if (N % B > 9 && B > 10)
			printf("%c", 'A' + N % B - 10);
		else
			printf("%d", N % B);
	}
}

int main() {

	int N, B;
	scanf("%d %d", &N, &B);

	binary(N, B);
	
	return 0;
}

