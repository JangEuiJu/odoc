#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	int t, n;
	int quarter, dime, nickel, penny;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		quarter = n / 25;
		dime = (n % 25) / 10;
		nickel = ((n % 25) % 10) / 5;
		penny = (((n % 25) % 10)) % 5 / 1;
		printf("%d %d %d %d\n", quarter, dime, nickel, penny);
	}

	return 0;
}