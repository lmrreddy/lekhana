#include<stdio.h>
int main ()
{
int a;
for(a=10;a<20;a=a+1)
{
printf("value of a:%d\n",a);
}
return 0 ;
}cmruuser@cmruuser:~/lekhana$ gcc d6.c
cmruuser@cmruuser:~/lekhana$ ./a.out
value of a:10
value of a:11
value of a:12
value of a:13
value of a:14
value of a:15
value of a:16
value of a:17
value of a:18
value of a:19
cmruuser@cmruuser:~/lekhana$ gcc d6.c
cmruuser@cmruuser:~/lekhana$ ./a.out
value of a:1
value of a:2
value of a:3
value of a:4
value of a:5
value of a:6
value of a:7
value of a:8
value of a:9

