# 1


# def lower(s):
# 	return s.lower()
# def upper(s):
# 	return s.upper()

# l = [
# "BicyclE",
# "BikE",
# "MopeD",
# "MotorbikE",
# "CaR",
# ]

# print(list(map(lower, l)))
# print(list(map(upper, l)))





#2-------------------------------------

# def my_square(num):
#     return num ** 2

# print ('enter nums: ')
# n = input()
# nums = list(map(int, n.split()))

# squared_numbers = list(map(my_square, nums))

# print(squared_numbers)



#3--------------------------------------
from sys import argv

index = 0
c = 0

def finder(text):
    if ind != -1:
        ind = text.find(' is ', ind)
        ind +=1
        count +=1
    return count

filename = argv[1]
text = open(filename, 'r')
l = text.read()
l = l.lower()


L = list(map(finder, l))

print(L)
print(count)


text.close()
