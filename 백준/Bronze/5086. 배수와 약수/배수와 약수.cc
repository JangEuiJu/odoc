#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*5086 배수와 약수*/
int main(){
	int n, m;

	while (1) {
		scanf("%d %d", &n, &m);

		if (n != 0 && m != 0) {
			if (m % n == 0)
				printf("factor\n");
			else if (n % m == 0)
				printf("multiple\n");
			else
				printf("neither\n");
		}
		else
			break;
	}

	return 0;
}