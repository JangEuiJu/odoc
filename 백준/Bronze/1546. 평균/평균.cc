#include <stdio.h>
#include <stdlib.h>

int main()
{	
	int n;
	double max = 0.0;
	double sum = 0.0;
	double a[1000] = { 0.0 };

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%lf", &a[i]);
		if (a[i] > max)
			max = a[i];
	}

	for (int i = 0; i < n; i++) {
		a[i] = a[i] / max * 100;
		sum += a[i];
	}
	printf("%lf", sum / n);
	
	return 0;
}