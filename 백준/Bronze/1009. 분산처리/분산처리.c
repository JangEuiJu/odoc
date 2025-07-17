#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
{
	int testcase; 
	scanf("%d", &testcase); 
	for (int i = 0; i < testcase; i++) 
	{
		int a, b;
		scanf("%d %d", &a, &b); 
		int task = a;
		for (int j = 1; j < b; j++) 
		{
			task = task * a %10;  
		}
		if (task % 10== 0) 
			printf("%d\n", 10);
		else 
			printf("%d\n", task % 10);
	}
}