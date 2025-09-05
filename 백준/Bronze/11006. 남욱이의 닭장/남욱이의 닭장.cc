#include <stdio.h>
 
int main() {
 
    int n, N, M;
    int U, T;
    scanf("%d", &n);
 
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &N, &M);
 
        U = M - (N - M);
        T = N - M;
 
        printf("%d %d\n", U, T);
    }
}