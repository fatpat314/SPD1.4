# """ Given an array of numbers and a target value of t. find two numbers that == t """
# # numbers == int, no negitive. list is sorted
# t = 9
# list = [3, 5, 7, 4, 12, 6]
#
# loop through list.
#
#  counter = n
#  snd-counter = m
#
#  list. loop through list, add first index to second.
#  repeat


# for i in list:
#     answer = list[n] + list[m]
#
#     if answer != t:
#         retrun list[n], list[m]
#
#         n = n++

"""Given a base 10 number, print the hexidecimal (base  16) representation of that number."""

16 == 0x10

input is base 10

123456789ABCDEF

def hex(n):
    if (n == 0):
        print(0)
    elif (n<=1):
        print(n)
    else:
        hex(n/16)

        decimal devided by 16 and store the result as int.
        16- the number = remainder

number = n
n/16, get remainder and keep track of the ramainder
get the result that resulted from deviding by 16 and devide that by 16
and repeat until we can no longer divide.

take the remainders that we saved and if one is over 9 conver to uhh hex letter.
