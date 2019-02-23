#include<stdio.h>
int main ()
{
int number;
printf("enter an integer:");
scanf("%d",&number);
if(number<0)
{
printf("you entered %d\n",number);
}
printf("the if statement is easy");
return 0;
}



output:
cmruuser@cmruuser:~/lekhana$ gcc d9.c
cmruuser@cmruuser:~/lekhana$ ./a.out
enter an integer:5
the if statement is easy
cmruuser@cmruuser:~/lekhana$ gcc d9.c
cmruuser@cmruuser:~/lekhana$ ./a.out
enter an integer:-1
you entered -1
the if statement is easy
cmruuser@cmruuser:~/lekhana$ gcc d9.c
cmruuser@cmruuser:~/lekhana$ ./a.out
enter an integer:34
you entered 34
the if statement is easy
