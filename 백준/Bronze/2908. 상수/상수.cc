#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char a[4];
	char b[4];
	char ap[4];
	char bp[4];
	int n1, n2;

	scanf("%s %s", a, b);
	for (int i = 0; i < 3; i++) {
		ap[i] = a[2 - i];
	}
	for (int i = 0; i < 3; i++) {
		bp[i] = b[2 - i];
	}
	ap[3] = '\0';
	bp[3] = '\0';
	
	n1 = atoi(ap);
	n2 = atoi(bp);

	if (n1 > n2)
		printf("%d", n1);
	else
		printf("%d", n2);
	

	return 0;
}