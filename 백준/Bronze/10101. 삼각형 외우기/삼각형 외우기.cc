#include <stdlib.h>
#include <string.h>
#include <malloc.h>


int main(){
	int a, b, c;
	int add;

	scanf("%d %d %d", &a, &b, &c);
	add = a + b + c;

	if (a == 60 && b == 60 && c == 60)
		printf("Equilateral");
	else if (add == 180 && (a == b || a == c || b == c))
		printf("Isosceles");
	else if (add == 180)
		printf("Scalene");
	else
		printf("Error");

	return 0;
}