#include <stdio.h>
 
int main() {
    int n;
    scanf("%d", &n);
    long long x = 0;
    int num = 0;
    while (n--)
    {
        long long sum = 0;
        scanf("%d", &num);
        for (int i = 0; i < num; i++)
        {
            scanf("%lld", &x);
            sum = (sum + x) % num;
        }
        if (sum % num == 0)
        {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }
    return 0;
}