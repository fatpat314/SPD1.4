# [flower, flow, flight]
# [tart, sam, court]
# def find_prefix(words_list, itr_index = 0, compare_index = 1, pass_prefix = None):
#     if compare_index == len(words_list) -1:
#         return pass_prefix
#     else:
#         for substring in words_list(itr_index) :
#             if substring in words_list(compare_index):
#                 prefix = '' + substring
#             if past_prefix == None:
#                 prefix = pass_prefix
#                 return find_prefix(words_list, itr_index+1, compare_index+1, pass_prefix)
#             elif prefix == pass_prefix:
#                 return find_prefix(words_list, itr_index+1, compare_index, pass_prefix)



# given a set of numbers, find 3 three numbers in that set that equal the target number


set = [1,2,3,4,5,6,7,8,9]
target = 6
comp1 = None
comp2 = None
# print(set)
def find_sum(set, target, comp1, comp2):
    for number in set:
        # print(n)
        comp1 = target - number
        # print(comp1, number)
        if comp1 in set:
        #     new_target = target - comp1
            print(comp1, number)
        # comp2 = new_target - comp1
        # print(comp2)
        # print("comp2",comp2)
        # print("new_target", new_target)
        # if comp2 and comp1 in set:
            # pass

            # print("output",comp1, comp2, number)
        # if comp2 in set:
            # break

    # if comp1 + comp2 + n == target:
        # print("TRUE", comp1, comp2, n)
find_sum(set, target, comp1, comp2)


        # pass

        # print(comp1)
# print(comp1, comp2)
