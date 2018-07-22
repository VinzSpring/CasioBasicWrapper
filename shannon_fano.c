#include <stdio.h>
#include "math.h"

//double numbers[6] = { 0.05, 0.05, 0.1, 0.2, 0.25, 0.35 };
double numbers[4] = { 0.1, 0.2, 0.3, 0.4 };

int code[255][255];
int split_index[100];

double count;
double err1 = 0;
double err2 = 0;

//sizeof(numbers)/sizeof(double)
int ind_start;
int ind_end;
int split_at;
int found_middle = 0;
int colum = 0;
int stack[255][3];
int stack_count = 0;
void find_middle() {
    count = 0;
    for (int i = ind_start; i < ind_end; i++) {
        if (found_middle) {
            code[i][colum] = 0;
        } else {
            code[i][colum] = 1;
        }
        //printf("%.2lf\n", numbers[i]);
        count += numbers[i];

        if (count >= 0.5 && !found_middle) {
            err1 = count - 0.5;
            err2 = fabs((count - numbers[i]) - 0.5);

            if (err1 > err2) {
                split_at = i;
            } else {
                split_at = i+1;
            }

            found_middle = 1;
            //printf("%.2lf\n", err1);
            //printf("%.2lf\n", err2);
            //printf("%d\n", split_index[0]);
        }
        
    }

    // Push next iteration
    stack_count++;
    colum++;

    stack[stack_count][0] = ind_start;
    stack[stack_count][1] = split_at - 1;
    stack[stack_count][2] = colum;

    stack[stack_count][0] = split_at;
    stack[stack_count][1] = ind_end;
    stack[stack_count][2] = colum;

    // Update variables
}


int main(int argc, char *argv[])  {

    ind_start = 0;
    ind_end = sizeof(numbers)/sizeof(double);

    find_middle();

    for (int i = 0; i < (sizeof(numbers)/sizeof(double)); i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d", code[i][j]);    
        }  
        printf("\n");
    }  


    return 0;
}