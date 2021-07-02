#4th practice task
num = int(input("enter: "))
i=1
while(i<num):
	print("num = ", i, '*', num//i%10, "	")
	i*=10



#homework
fizz = int(input())
buzz = int(input())
num = int(input())

for i in range (1, num+1):
	if(not(i%fizz and i%buzz)):
		print("FB ")
	elif(not i%buzz):
		print('B ')
	elif(not i%fizz):
		print('F ')
	else:
		print(i, ' ')
		