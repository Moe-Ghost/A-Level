import sys
from random import randint as rand 

start = open("start.txt", "w+")
final= open("final.txt", "w")



for i in range(20):
	start.write(str(rand(2, 3)) + ' ')
	start.write(str(rand(4, 7)) + ' ')
	start.write(str(rand(10, 15)) + '\n')
start.seek(0)
for line in start.readlines():
	list = []
	line= line.split()
	for i in range(len(line)):
		line[i]=int(line[i])
	for j in range(1, line[-1]+1):
		if not j%line[0] and not j%line[1]:
			list.append("FB ")
		elif not j%line[0]:
			list.append("F ")
		elif not j%line[1]:
			list.append("B ")
		else:
			list.append(str(j)+' ')

	for item in list:
		final.write("%s" % item)
	final.write('\n')

start.close()
final.close()