# Given a sorted array, remove the duplicates
"""Complexity: 0(n), loop dependent on the length of the array"""
def remove_duples(arr):
    new_array = []
    for i in arr:
        if i not in new_array:
            new_array.append(i)
    return new_array

arr = [1, 2, 2, 3, 4, 4]
print(remove_duples(arr))

"""Complexity: 0(n), putting the array into a dict is dependent on the size of the array"""
def remove_duples(arr):
    dict = {}
    my_arr = []
    for i in arr:
        if i not in dict:
            dict[i] = True
            my_arr.append(i)
    return my_arr

arr = [1, 2, 2, 3, 4, 4]
print(remove_duples(arr))

"""Complexity: 0(n**2), first loop is dependent on the size of the array and the append
method is also depended on the length of the inputs"""
def merge_arrays(array1, array2):
    i = 0
    j = 0
    new_array = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            new_array.append(array1[i])
            i += 1
        else:
            new_array.append(array2[j])
            j += 1
    if i == len(array1):
        new_array.extend(array2[j:])
    elif j == len(array2):
        new_array.extend(array1[i:])

    return new_array

arr1 = [1,4,5,7,8,32]
arr2 = [2,3,4,11,15,17]
print(merge_arrays(arr1, arr2))



""" rotating an array. In place complete on right rotation of a list """

""" assumptions: array of things """

""" list,
loop through indexes of list.
save the next value of the index.
put OG value into its following index
and repete with the saved value.
"""
"""Complexity: 0(n), dependent on the length of input"""
arr = ["cats","morecats","anothercat"]
def right_rotation(arr):

    save = arr[0]
    for i in range(len(arr)):
        if i < len(arr)-1:
            arr[i] = arr[i+1]
    arr[-1] = save

print(right_rotation(arr))
print(arr)


"""reversed loop"""
print(list(range(len(arr)-1,-1,-1)))
