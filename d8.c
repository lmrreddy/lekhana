#include<stdio.h>
int main ()
{
int j=0;
do
{
printf("value of variable j is :%d\n",j);
j++;
}
while(j<=3);
return 0;
}


output:
cmruuser@cmruuser:~/lekhana$ gcc d8.c
cmruuser@cmruuser:~/lekhana$ ./a.out
value of variable j is :0
value of variable j is :1
value of variable j is :2
value of variable j is :3

