# num = int(input("enter num "))
# while(num % 2 != 1 or num <= 0):
# 	num = int(input('Enter enother num: '))

# for i in range(1, num + 1, 2):
# 	print(' ' * ((num - i)//2), '*' * i)
# for i in range(num - 2, 0, -2):
# 	print(' ' * ((num - i)//2), '*' * i)




# def func(flat_num, flat_on_floor, floor_num):

# 	entrance = flat_num // (flat_on_floor * floor_num)
# 	floor = (flat_num - (flat_on_floor * floor_num) * entrance) // flat_on_floor

# 	if flat_num % entrance*floor == 0:
# 		entrance -= 1
# 		floor += floor_num
	
# 	return (floor, entrance)


# floor_num = int(input('Кол-во этажей: '))
# flat_on_floor = int(input('Кол-во квартир на этаж: '))
# flat_num = int(input('Номер квартиры: '))



# addres = func(flat_num,flat_on_floor,floor_num)

# print("Этаж: ",addres[0], "\nПодъезд: ", addres[1])



file = open('nums.txt', "r")

text = file.readlines()

for line in text:
	avrg = 0
	L = []
	line = line.rstrip()
	line = line.split()
	line = 
	print(line)

	# L = [int(j) for i in line for j in i if j != ';']
	# print(L)


