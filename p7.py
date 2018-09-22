import random
while True:
	 n=input("enter r to roll the dice and q to quit")
	 if(n=='q'):
	 	print("bye")
	 	exit()
	 elif(n=='r'):
	 	r=random.randint(1,6)
	 	print(r)
dl309@soetcse:~/lekhana$ python3 p7.py
enter r to roll the dice and q to quitr
6
enter r to roll the dice and q to quitr
5
enter r to roll the dice and q to quitr
3
enter r to roll the dice and q to quitr
6
enter r to roll the dice and q to quitr
5
enter r to roll the dice and q to quitr
4
enter r to roll the dice and q to quitr
1
enter r to roll the dice and q to quitr
6
enter r to roll the dice and q to quitq
bye

