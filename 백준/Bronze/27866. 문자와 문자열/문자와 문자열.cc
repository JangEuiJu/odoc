#include <stdio.h>
#include <stdlib.h>

int main()
{	
	char s[1000];
	int n;
	
	scanf("%s %d", &s, &n);
	printf("%c", s[n - 1]);

	return 0;
}