/* Portable C version of the mutual-exclusion demonstration.
   The original manual uses Turbo C functions (conio.h, kbhit, getch).
   This version runs with a standard C compiler. */
#include <stdio.h>

int main(void) {
    int n, i;
    int critical_section = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        if (critical_section == 0) {
            critical_section = 1;
            printf("Process %d entered critical section.\n", i);
            printf("Process %d exited critical section.\n", i);
            critical_section = 0;
        } else {
            printf("Process %d is waiting.\n", i);
        }
    }
    return 0;
}
