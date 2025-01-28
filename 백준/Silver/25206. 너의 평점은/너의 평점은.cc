#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>


int main(void){
	double final;
	double sum = 0;
	double scores = 0;

	typedef struct {
		char subject[50];
		char myScore[3];
		double credit;
	} grade;

	grade array[20];

	for (int i = 0; i < 20; i++) {
		scanf("%s %lf %s", &array[i].subject, &array[i].credit, &array[i].myScore);
		if (strcmp(array[i].myScore, "P") != 0)
			sum += array[i].credit;
		if (strcmp(array[i].myScore, "A+") == 0)
			scores += array[i].credit * 4.5;
		else if (strcmp(array[i].myScore, "A0") == 0)
			scores += array[i].credit * 4.0;
		else if (strcmp(array[i].myScore, "B+") == 0)
			scores += array[i].credit * 3.5;
		else if (strcmp(array[i].myScore, "B0") == 0)
			scores += array[i].credit * 3.0;
		else if (strcmp(array[i].myScore, "C+") == 0)
			scores += array[i].credit * 2.5;
		else if (strcmp(array[i].myScore, "C0") == 0)
			scores += array[i].credit * 2.0;
		else if (strcmp(array[i].myScore, "D+") == 0)
			scores += array[i].credit * 1.5;
		else if (strcmp(array[i].myScore, "D0") == 0)
			scores += array[i].credit * 1.0;
		else if (strcmp(array[i].myScore, "F") == 0)
			scores += array[i].credit * 0.0;
		
	}
    
	final = scores / sum;
	printf("%f", final);

	return 0;
}