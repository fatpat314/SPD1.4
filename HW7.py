"""Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward."""

"""Restate question"""
# Is the input the same backward and forward?
# return bool

"""Clearifying questions"""
# Are there negitive numbers?

"""Assumptions"""
# There are negitive numbers

"""Brain storming"""
# A search working form both ends moving in would work.
# I could do this iteritivly with a time complexity of O(n).
# But depending on the length of the input it could be faster with recursion.
# I will try it with recursion

def is_palindrome(numbers, front = None, back = None):
    numbers = str(numbers)
    numers = numbers.replace("-", "")
    num_list = list(numbers)
    print(num_list)

    # make a pointer for the front index and back index

    if front == None and back == None:
        front = 0
        back = len(num_list) -1
        print(front,back)
        truth = None

    if front < back:
        # check if those pointers match
        if num_list[front] != num_list[back]:
            truth = False
            print(front,back)
            # if they dont: return false
            return truth

        else:
            # if they do, call resursion add one to front index and minus one form back index
            is_palindrome(numbers, front + 1, back - 1)
            truth = True
        return truth

# print(is_palindrome(12345))
# print(is_palindrome(12321))

"""Follow up"""
# I think this works well. I needed to go back and take care of negitive cases
# Could I have solved it without converting input to strings?
# Not as easily, and not with the same time complexity. I would need to figure out
# a way to loop over integers putting the individual number into a list. Or if I made
# the input a list. But then the input would be a different data type. But how would
# you do this with out having the input be a list if we wanted to see compare say 12,2,34,43,2,21?





"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid."""
"""Restate question"""
# We get a string. We need to make sure all of the opening characters are closed
# and all the closed characters were opened
"""Clearifying questions"""
# Seems clear to me

"""Brain storming"""
# I think a similar search that is done in is_palindrome might work if
# we set flags for when to anotate when something is opened and closed.
# So manybe start with a back and a front and if we meet an opener or closer
# set the flag to false until that item is closed







def check_brackets(expression):
    # going to push open on stack
    # if find an end compate to top of stack
    open_brackets = ["{","[","("]
    closed_brackets = ["}","]",")"]
    bracket_stack = []

    for character in expression:
        if character in open_brackets:#add open bracket to stack
            bracket_stack.append(character)
        if character in closed_brackets:
            bracket_stack.append(character)
        if len(bracket_stack) != 0:
            print("check1")
            return False
        position = closed_brackets.index(character)

        open_bracket_at_top = bracket_stack.pop(len(bracket_stack) -1)

        # check if the open bracket at the
        if open_bracket_at_top != open_brackets[position]:
            print("check2")
            return False
    if len(bracket_stack)==0:
        return True
    else:
        print("check")
        return False
print(check_brackets("(({{}}))"))








# def is_valid(str):
#     open = ['(','{','[']
#     close = [')','}',']']
#     truth = None
#     stack = []
#     for i in str:
#         if i in open:
#             stack.append(i)
#         if i in close:
#             if len(bracket_stack != 0):
#                 print("HERE")
#                 return False
#             position = close.index(i)
#             open_at_to_of_stack = stack.pop(len(stack)-1)
#
#             if open_at_to_of_stack != open[position]:
#                 print("TEST")
#                 return False
#         if len(stack) == 0:
#             return True
#         else:
#             print(stack)
#             print("what")
#             return False
#
# print(is_valid("()"))








# """Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999."""
#
# """Restate question"""
# # Convert the input string character to a integer.
#
# """Clearifying questions"""
# # Null
#
# """Assumptions"""
# # I think this is pretty straight forward
#
# """Brain storming"""
# # So I would need to take the input string and make it into a list.
# # I will then want to loop over the list and convert the value of each
# # index to the corrisponding arabic numeral value.
# # There could be a way to do this recursively, but because roman numerals are going
# # to generally be a low number of character inputs, itteration would not take much longer is at all
# # time complexity of O(n)
#
# def convert_romans(numerals):
#     # print(numerals)
#     numeral_list = list(numerals)
#     # print(numeral_list)
#     number_list = []
#     print(numeral_list)
#     for i in range(len(numeral_list)):
#         print("here")
#         # is there a way to do it with out a bunch of is statments?
#         print(numeral_list[i])
#         if numeral_list[i] == "I":
#             i = 1
#             number_list.append(i)
#         elif numeral_list[i] == "V":
#             i = 5
#             number_list.append(i)
#         elif numeral_list[i] == "X":
#             i = 10
#             number_list.append(i)
#         elif numeral_list[i] == "L":
#             i = 50
#             number_list.append(i)
#         elif numeral_list[i] == "C":
#             i = 100
#             number_list.append(i)
#         elif numeral_list[i] == "D":
#             i = 500
#             number_list.append(i)
#         elif numeral_list[i] == "M":
#             i = 1000
#             number_list.append(i)
#     print(number_list)
#     # print(number_list[0] + number_list[1])
#     ans = 1
#     for i in range(len(number_list)):
#         if i < len(number_list)-1:
#             ans = ans + number_list[i]
"""Roman numerals dont work like this. How would I get the numerals to
recognize when an I before a V is 4 and when it is 1 and 5?"""
#             # print(ans + number_list[i+1])
#     print(ans)

# convert_romans("IX")
