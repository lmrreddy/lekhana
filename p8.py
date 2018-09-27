import random
count=0
while True:
	n=input("press r to roll and q to quit")
	if(n=='q'):
		print("bye")
		exit()
	elif(n=='r'):
		r=random.randint(1,6)
		print("value of r",count)
		count=count+r
		print("score is",count)
		if(count==8):
			count=37
			print("hurray!you got a ladder")
		elif(count==11):
			count=2
			print("oh no,you got bit")
		elif(count==13):
			count=34
			print("hurray!you got a ladder")
		elif(count==25):
			count=4
			print("oh no,you got bit")
		elif(count==38):
			count=9
			print("oh no, you got bit")
		elif(count==40):
			count=68
			print("hurray!you got a ladder")
		elif(count==52):
			count=81
			print("hurray!you got a ladder")
		elif(count==65):
			count=46
			print("oh no,you got bit")
		elif(count==76):
			count=97
			print("hurray!you got a ladder")
		elif(count==89):
			count=70
			print("oh no,you got bit")
		elif(count==93):
			count=64
			print("oh no,you got bit")
		elif(count==100):
			print("you won")
	else:
		break