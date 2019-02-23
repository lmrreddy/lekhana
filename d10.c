#include<stdio.h>
int main ()
{
int number;
printf("enter an integer:");
scanf("%d",&number);
if(number%2==0)
printf("%d is even integer",number);
else
printf("%d is odd integer",number);
return 0;
}

output:
cmruuser@cmruuser:~/lekhana$ gcc d10.c
cmruuser@cmruuser:~/lekhana$ ./a.out
enter an integer:55    
55 is odd integer
cmruuser@cmruuser:~/lekhana$ gcc d10.c
cmruuser@cmruuser:~/lekhana$ ./a.out
enter an integer:44
44 is even integer
