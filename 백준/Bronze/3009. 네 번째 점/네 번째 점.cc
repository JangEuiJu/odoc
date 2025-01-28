#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
	int fx, fy;
	typedef struct {
		int x;
		int y;
	} element;
	element rectangle[3];
	for (int i = 0; i < 3; i++) {
		scanf("%d %d", &rectangle[i].x, &rectangle[i].y);
	}

	if (rectangle[0].x == rectangle[1].x)
		fx = rectangle[2].x;
	else if (rectangle[0].x == rectangle[2].x)
		fx = rectangle[1].x;
	else if (rectangle[1].x == rectangle[2].x)
		fx = rectangle[0].x;

	if (rectangle[0].y == rectangle[1].y)
		fy = rectangle[2].y;
	else if (rectangle[0].y == rectangle[2].y)
		fy = rectangle[1].y;
	else if (rectangle[1].y == rectangle[2].y)
		fy = rectangle[0].y;
	
	printf("%d %d", fx, fy);


	return 0;
}