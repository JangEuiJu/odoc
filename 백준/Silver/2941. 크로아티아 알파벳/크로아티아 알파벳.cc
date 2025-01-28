#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>


int main() {
	char input[101];
	int count = 0;

	scanf("%s", input);

	for (int i = 0; input[i] != '\0'; i++) {
		switch (input[i]) {
		case 'c': 
			if (input[i + 1] == '=' || input[i + 1] == '-') 
				i++;
			count++;
			break;
		case 'd' :
			if (input[i + 1] == '-') 
				i++;
			else if (input[i + 1] == 'z' && input[i+2] == '=')
					i = i + 2;
			count++;
			break;
		case 'l':
		case 'n':
			if (input[i + 1] == 'j') 
				i++;
			count++;
			break;
		case 's':
		case 'z':
			if (input[i + 1] == '=')
				i++;
			count++;
			break;
		default :
			count++;
		}
	}

	printf("%d", count);
	return 0;
}


