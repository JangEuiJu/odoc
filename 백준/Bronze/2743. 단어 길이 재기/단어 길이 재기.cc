#include <stdio.h>
#include <stdlib.h>

int main()
{	
	char s[1000];
	int i = 0;
	
	scanf("%s", &s);
	while (s[i] != '\0') {
		i++;
	}
	printf("%d", i);

	return 0;
}