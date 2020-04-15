# Question 1
"""Your task is to convert a number into a string that contains
raindrop sounds corresponding to certain potential factors.
A factor is a number that evenly divides into another number,
leaving no remainder. The simplest way to test if a one number i
s a factor of another is to use the modulo operation."""

"""The rules of raindrops are that if a given number:

has 3 as a factor, add 'Pling' to the result.
has 5 as a factor, add 'Plang' to the result.
has 7 as a factor, add 'Plong' to the result.
does not have any of 3, 5, or 7 as a factor,
the result should be the digits of the number."""

# Take in two int's and based on the result of the modulous return string
# input: n
# n % number = string
# output: Plong

"""to make things more interesting, I am adding a 2nd input number"""

def raindrops(n):
    result = ""
    # m = 28
    ans = n
    # print(ans)
    if ans % 3 == 0:
        result = result + "Pling"
        # print(result)
        # return result

    if ans % 5 == 0:

        result = result + "Plang"
        print(result)


    if ans % 7 == 0:
        result = result + "Plong"
        # print(result)
        print(result)

    if ans % 3 or ans % 5 or ans % 7 == 0:
        print(ans)

# print(raindrops(22))


# Q2

"""Manage a game player's High Score list.

Your task is to build a high-score component of the classic
 Frogger game, one of the highest selling and addictive games
 of all time, and a classic of the arcade era. Your task is to
 write methods that return the highest score from the list, the
 last added score and the three highest scores."""

 # Make a list that updates the latest input
 # return Three highest scores and the last added score

# inputs: int
# output: score 1, score 2, score3. latest score
arr = [5,4,3,2,6,7,8,5,3,6,7]

def scoreboard(n):
    # arr = []
    arr.append(n)
    print("Latest Score: ", arr[-1])

    arr.sort()
    print("HIGH SCORES")
    print("#1: ", arr[-1])
    print("#2: ", arr[ -2])
    print("#3: ", arr[-3])



scoreboard(3)
