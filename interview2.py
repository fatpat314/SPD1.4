# '''Find the longest substring of unique letters in a given string of n letters.'''
#
# # Input: string: ex. "Mississippi"
#
# # Output: string:
#
#
# str = "Homework"
#
# """Loop over the string and check the char and see if we saw it before"
# "if not then we can assume that it is a unique value"
# "then we need to keep going and see how long the substring remains unique"
# "return the longest substring"""
#
# def substring(str):
#     #use this to keep track of longest substring
#     dict = {}
#
#     for char in str:
#         substr = ""
#         # if not in dict,key(), add char to dict
#         # if it is, we need to save the substr and delete the common char
#         if char in dict.keys():
#             substr = substr + char
#         else:
#             dict[char] = 1
# """Given an array a of numbers and a target value t, find two numbers that sum to t (that is, a[i] + a[j] = t)."""
#
# [1,2,3,4,5,6,7,8,9] target = 16
#
# Output: 7, 9
#
# """Loop through array, i - target. search through the array again for the diff."""
# """ """

def ans(array, t):
    dict = {}
    for i, value in enumerate(array): #allows you to look into the index and the value
        ans = t - value
        # print(ans)
        if value + value == t:
            return value, value
        if ans in dict.keys():
            return ans, value

        else:
            dict[value] = i

print(ans([1,2,3,4,5,6,7,8,9], 16))
