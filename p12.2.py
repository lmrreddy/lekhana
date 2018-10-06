'''def printBoard():
	print("|1|2|3|")
	print("_______")
	print("|4|5|6|")
	print("_______") 
	print("|7|8|9|") 
	print("_______")
printBoard()'''

a=[1,2,3,4,5,6,7,8,9]
def printBoard():
	print('|',a[0],'|',a[1],'|',a[2],'|')
	print('___________')
	print('|',a[3],'|',a[4],'|',a[5],'|')
	print('___________')
	print('|',a[6],'|',a[7],'|',a[8],'|')
	print('___________')

playeronetrun = True
while True:
	printBoard()
	p=int(input("choose your place >>"))
	if(p in a):
		if playeronetrun:
			#p=input("choose your place,player 1 >>" )
			print("player 1 chose:",p)
			a[p-1]='X'
			playeronetrun = not playeronetrun
		else:
			#p=input("choose your place,player 2 >>" )
			print("player 2 chose:",p)
			a[p-1]='O'
			playeronetrun =not playeronetrun
		#checking winning conditions:
		for i in (0,3,6):
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				if a[i]=='X':
					print("player 1 wins")
					exit()
				else:
					print("player 2 wins")
					exit()
		for i in range(3):
			if(a[i]==a[i+3] and a[i]==a[i+6]):
				if a[i]=='X':
					print("player 1 wins")
					exit()
				else:
					print("player 2 wins")
					exit()
	else:
		continue