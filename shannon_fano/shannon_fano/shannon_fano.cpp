#include <stdio.h>
#include "math.h"
#include <iostream>

//double numbers[6] = { 0.05, 0.05, 0.1, 0.2, 0.25, 0.35 };
//double numbers[4] = { 0.1, 0.2, 0.3, 0.4 };
double numbers[8] = { 0.05, 0.06, 0.08, 0.10, 0.12, 0.14, 0.15, 0.30 };

int code[255][255];

double count = 0;
double err1 = 0;
double err2 = 0;
double sum = 0;

int stack[255][3];
int stack_count = -1;

int ind_start = 0;
int ind_end = 0;
int colum = 0;

int split_at = 0;
int found_middle = 0;

void find_middle() {
	// Update variables
	ind_start = stack[stack_count][0];
	ind_end = stack[stack_count][1];
	colum = stack[stack_count][2];

	// Reset vars
	count = 0;
	found_middle = 0;

	// Break condition
	if (ind_start >= ind_end) {
		stack_count--;
		return;
	}

	// Interval consist of two items
	if (ind_end - ind_start == 1) {
		code[ind_start][colum] = 1;
		code[ind_end][colum] = 0;
		stack_count--;
		return;
	}

	// Get actual item sum
	sum = 0;
	for (int k = ind_start; k <= ind_end; k++) {
		sum += numbers[k];
	}

	for (int i = ind_start; i <= ind_end; i++) {

		if (found_middle) {
			code[i][colum] = 0;

		} else {
			code[i][colum] = 1;
		}

		count += numbers[i];

		if (count >= (sum* 0.5f) && !found_middle) {
			err1 = count - (sum* 0.5f);
			err2 = fabs((count - numbers[i]) - (sum* 0.5f));

			if (err1 <= err2) {
				split_at = i;

			} else {
				split_at = i - 1;
				code[i][colum] = 0;
			}

			found_middle = 1;
		}
	}

	// Push next iteration
	colum++;

	// Dont increase stack to simulate 'pop' iteration
	stack[stack_count][0] = ind_start;
	stack[stack_count][1] = split_at;
	stack[stack_count][2] = colum;

	stack_count++;
	stack[stack_count][0] = split_at + 1;
	stack[stack_count][1] = ind_end;
	stack[stack_count][2] = colum;
}


void fillarray() {
	for (int i = 0; i < 255; i++) {
		for (int j = 0; j < 255; j++) {
			code[i][j] = 7;
		}
	}
}

int main(int argc, char *argv[]) {

	fillarray();

	// Init first iteration
	stack_count++;
	stack[stack_count][0] = 0;
	stack[stack_count][1] = (sizeof(numbers) / sizeof(double)) - 1;
	stack[stack_count][2] = 0;


	while (stack_count > -1) {
		find_middle();
	}

	for (int i = 0; i < (sizeof(numbers) / sizeof(double)); i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d", code[i][j]);
		}
		printf("\n");
	}

	getchar();
	return 0;
}