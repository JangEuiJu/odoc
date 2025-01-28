#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

	int length, check = 1;
	char s[100];
	char reverse[100];

	scanf("%s", s);
	length = strlen(s);

	for (int i = 0; i < length; i++) {
		reverse[i] = s[length-i-1];
	}

	for (int i = 0; i < length; i++) {
		if (s[i] != reverse[i])
			check = 0;
	}
	
	printf("%d", check);
	
}