#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>


int main(void){
	char n[100];
	int b;
	scanf("%s %d", n, &b);
	int sum = 0;
	for (int i = 0; n[i] != 0; i++) {
		if (n[i] >= 'A' && n[i] <= 'Z') {
			sum = sum * b + (n[i] - 'A' + 10);
		}
		else {
			sum = sum * b + (n[i] - '0');
		}
	}

	printf("%d", sum);

	return 0;
}