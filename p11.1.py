import random
r={1:'r',2:'p',3:'s'}
p1=r[random.randint(1,3)]
print(p1)
a=0
b=0
while a<3 and b<3:
	p2=input("enter your choice r/p/s or q to quit")
	if p2=='q':
		print("you quit")
		exit()
	if p2==p1:
		print("its a tie!!")
	elif p2=='r':
		if p1=='p':
			print("p2 gets the point")
			b=b+1
			print(b)
		else:
			print("p1 gets the point")
			a=a+1
			print(a)
	elif p2=='p':
		if p1=='r':
			print("p2 gets the point")
			b=b+1
			print(b)
		else:
			print("p1 gets the point")
			a=a+1
			print(a)
	elif p2=='s':
		if p1=='p':
			print("p1 gets the point")
			a=a+1
			print(a)
		else:
			print("p2 gets the point")
			b=b+1
			print(b)
	if a==3:
		print("p1 won the game")
	elif b==3:
		print("p2 won the game")