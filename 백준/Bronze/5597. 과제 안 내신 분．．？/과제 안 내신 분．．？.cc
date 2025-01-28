#include <stdio.h>
#include <stdlib.h>

int main()
{	
	int n;
	int a[30] = { 0 };
	for (int i = 0; i < 28;  i++) {
		scanf("%d", &n);
		a[n - 1] = 1;
		
	}
	
	for (int i = 0; i < 30; i++) {
		if (a[i] == 0) {
			printf("%d\n", i + 1);
		}
	}

	return 0;
}