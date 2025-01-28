#include <stdio.h>

int main()
{
    int arr;
    int max =0;
    int n=0; //0으로 초기화해야 함
    int m=0; //0으로 초기화해야 함 
    //-> 9x9숫자가 0일때 n+1은 n에 쓰레기 값이 들어가 있음(오류)
   
    for(int i=0;i<9;i++){
        for(int j=0; j<9; j++){
            scanf("%d", &arr); 
            if(max < arr){
                max = arr;
                n=i;
                m=j;
            }
        }
    }
  
    printf("%d\n",max);
    printf("%d %d\n",n+1,m+1);
    
    return 0;
}