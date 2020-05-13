"""Matching pairs"""
# Find the two numbers in a list that match out target number when added together.
def find_pairs(values, target):
    if target > 1:
        value_dict = {}
        for value in values:
            if value in value_dict:
                value_dict[value] += 1
            else:
                value_dict[value] = 0

        print(value_dict)
        for value in values:
            target_compliment = target - value
            print ("target compliment:", target_compliment)
            print("value:", value)
            print("target:",target)
            if target_compliment in value_dict:
                if target_compliment == value:
                    if not value_dict[target_compliment] > 0:
                        continue
                return str(value) + " and " + str(target_compliment)

        return "No valid pairs"

"""Tests"""
# print (find_pairs([14, 13, 6, 7, 8, 10, 1, 2], 3)) =="1 and 2"
# print(find_pairs([14, 13, 6, 7, 8, 10, 1], 3)) == "No valid pairs"
# print(find_pairs([2,2], 4) == "2 and 2")
# print(find_pairs([2], 4))
# print(find_pairs([2], -1) == "No valid pairs")
# print(find_pairs([14, 13, 6, 7, 8, 10, 1], 0) == "No valid pairs")
# print(find_pairs([14, 13, 6, 7, 8, 10, 1], 1) == "No valid pairs")
# print find_pairs([], 4) == "No valid pairs"

"""Max consecutive sequence"""
# given a list of ints L. Find the max length of a sequence of
# consecutive numbers that can be formed using elements from L
