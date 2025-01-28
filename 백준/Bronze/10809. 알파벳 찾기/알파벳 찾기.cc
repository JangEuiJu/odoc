#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{	
	char s[100];
	int a[26];
	scanf("%s", s);

	for (int i = 0; i < 26; i++) {
		a[i] = -1;
	}

	for (int c = 'a'; c <= 'z'; c++) {
		for (int i = 0; i < strlen(s); i++) {
			if (s[i] == c) {
				a[s[i]-'a'] = i;
				break;
			}
		}
	}
	
	for (int i = 0; i < 26; i++) {
		printf("%d ", a[i]);
	}


	return 0;
}