#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{	
	char s[100];
	int n, sum = 0;

	scanf("%d", &n);
	scanf("%s", s);

	for (int i = 0; i < n; i++) {
		sum += s[i] - '0';
	}
	printf("%d", sum);

	return 0;
}