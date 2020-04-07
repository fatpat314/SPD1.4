# Q1
"""Given an array of integers, return indices of the two numbers
such that they add up to a specific target"""

# restate question
'''So we have an array of ints. we want to return the position of the index
of two numbers that add to our target number'''

# clearifying questions
'''None'''

# assumptions
'''No negitive numbers, list is sorted'''

# brainstorm
'''hokay, so the example that is given is [2, 7, 11, 15], and the target = 9'''
'''The first thing to come to mind is to loop over our list and check the indices
to see if they add to the target. "for i in list, for j in list, j == i or j and i ++"'''
'''But I think the better way to do it would be to find the differential and see if
that it exists in the list'''

list = [2, 7, 11, 15]
target = 17
count = 0

def search(list, target):
    for i in list:
        first = list.index(i)
        diff = target - i
        if diff in list:
            second = list.index(diff)
            if diff + i == target:
                print('Your first index is ' + str(first))
                print('Your second index is ' + str(second))


                return diff, i
        else:
            print("Does not exist in list")
print(search(list, target))

# recap/analysis
''' The way that I did it works well I think. It runs at a time complexity of O(n)
I think if I were to use my first solution it would of had a complesity of O(n**2).
Binary search would have been an interesting way to go, I am not sure if it would have
been anymore time efficient.'''






# Q2
"""Given a 32-bit signed integer, reverse digits of an integer."""

# restate question
'''We will be givin a integer, and we need to reverse the digits'''

# clearifying questions
'''What do you mean by "32-bit signed integer"?, is the int negitive?'''

# brainstorm
'''Ummm, there is just a fancy command I could do. But lets try not to use it.
digits = digits[::-1]
So with that in mind, lets try to make it into a new list.'''

input = 123
def reverse(input):
    list = []
    input = str(input)
    # input = list(input)
    n = -1
    for i in range(len(input)):
        list.append(str(input[n]))
        n-=1
        string = ""
        join = string.join(list)
    print(join)
print(reverse(input))

# recap/analysis
'''I would have much rathe used that command, but this would generally work except
I think the time complexity would be O(n**2) due to the dependent loop and the append
is also dependent on the size of the input'''
