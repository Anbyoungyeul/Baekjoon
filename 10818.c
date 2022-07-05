#include<stdio.h>

int main(void)
{
    int n=0, count=0, min=100000, max=-100000; // 최댓값 최솟값 설정
    scanf("%d", &count); // %d, %s 구분
    for(int i=0;i<count;i++) //입력받은 횟수 만큼
    {
        scanf("%d", &n);
        if(n>max) // 최댓값 업데이트
            max=n;
        if(n<min) //최솟값 업데이트
            min=n;
    }
    printf("%d %d", min,max); 
    return 0;
}
