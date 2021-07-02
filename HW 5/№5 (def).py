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
import sys

def count(text):
    if text.find('is'):
        return 



# file = sys.argv[1]
text = open("№5.txt", 'r')

print(text[1].find('is'))

text.close()
