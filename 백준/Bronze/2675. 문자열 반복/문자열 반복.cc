#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{	
	int n1, n2;
	char s[20];

	scanf("%d", &n1);

	for (int i = 0; i < n1; i++) {
		scanf("%d %s", &n2, s); 
		for (int j = 0; j < strlen(s); j++) {
			for (int k = 0; k < n2; k++) {
				printf("%c", s[j]);
			}
		}
		printf("\n");
	}
	

	return 0;
}