# def marks():
#	L =[]
# 	for i in range(5):
# 		L.append(rand(1,5))
# 	return L


# from random import randint as rand

# names = dict.fromkeys(["Vova", "Daniil", "Stas", "Vasya"])

# for name in names:
# 	names[name] = marks()


# max_ = 0
# wors_stud = ''
# best_stud = ''
# min_ = 6
# avrg = 0
# for name, mark in d.items():
# 	for i in range(0, len(mark)-1):
# 		avrg += mark[i]
# 	avrg //= len(mark)
# 	if avrg < min_:
# 		min_ = avrg
# 		wors_stud = name
# 	elif avrg > max_:
# 		max_ = avrg
# 		best_stud = name

# print(d, '\n',wors_stud, ':', min_, '\n', best_stud, ':', max_)

print("Hui loha ebanoe govno")



def timetable(title):
	L =[]
	while len(L) < rand(1,3):
		r = title[rand(0, 5)]
		if r not in L:
			L.append(r)
	return L


from random import randint as rand

courses = dict.fromkeys(['Python', 'FrontEnd', 'FullStack', 'Java'])
names = ["Vova", "Daniil", "Stas", "Vasya", "Nikita", "Pavel"]

for course in courses:
	courses[course] = timetable(names)

print(courses, '\n\n')

for course in courses:
	if len(courses[course]) > 1:
		print(course, ': ', len(courses[course]))


not_front = []
for course in courses:
	for name in courses[course]:
		for i in range(0, len(courses['FrontEnd'])):
			if name != courses['FrontEnd'][i]:
				not_front.append(name)

print(set(not_front))

py_java = []
for course in courses:
	for name in courses[course]:
		for i in range(0, len(courses['Python'])):
			if name == courses['Python'][i]:
				py_java.append(name)
		for i in range(0, len(courses['Java'])):
			if name == courses['Java'][i]:
				py_java.append(name)

print(set(py_java))


# d = {
# 'XXS': [42, 36, 8, 38, 24],
# 'XS': [44, 38, 10, 40, 26],
# "S": [46, 40, 12, 42, 28],
# "M": [48, 42, 14, 44, 30],
# "L": [50, 44, 16, 46, 32],
# "XL": [52, 46, 18, 48, 34],
# "XXL": [54, 48, 20, 50, 36],
# "XXXL": [46, 50, 22, 52, 38]
# }

# print('enter inernational size: XXS, XS, S, M, L, XL, XXL, XXXL')
# size = str(input())
# print('enter country:\nR: 1\nGER: 2\nUSA: 3\nFR: 4\nBR: 5\n')
# country = int(input())

# print(d[size][country-1])
