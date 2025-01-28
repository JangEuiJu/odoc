#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>


int main(void){
	int x, y, w, h;
	int minX = 1000;
	int minY = 1000;
	int result = 0;
	scanf("%d %d %d %d", &x, &y, &w, &h);

	if (x < w - x)
		minX = x;
	else
		minX = w - x;

	if (y < h - y)
		minY = y;
	else
		minY = h - y;

	if (minX < minY)
		result = minX;
	else
		result = minY;

	printf("%d", result);

	return 0;
}