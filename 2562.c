#include<stdio.h>

int main(void)
{
    int num[9];
    int max=0, count;
    for(int i=0;i<9;i++)
    {
        scanf("%d", &num[i]);
        if(max < num[i])
        {
            max=num[i];
            count = i;    
        }
    }
    printf("%d\n%d", max, count+1);
    return 0;
}
