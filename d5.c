#include<stdio.h>
int main()
{
 int a=9,b=4,c;
 c=a+b;
 printf("a+b=%d\n",c);
 c=a-b;
 printf("a-b=%d\n",c);
 c=a*b;
 printf("a*b=%d\n",c);
 c=a/b;
 printf("a/b=%d\n",c);
 c=a%b;
 printf("remainder when divided by b=%d\n",c);
 return 0;
}
//output:
cmruuser@cmruuser:~$ gcc d5.c
cmruuser@cmruuser:~$ ./a.out
a+b=13
a-b=5
a*b=36
a/b=2
remainder when divided by b=1//
