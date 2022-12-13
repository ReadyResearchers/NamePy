# Author: Jessica Strait
# This is an exercise in the set data type: an unordered group of elements in which no element repeats.
# The first program will take a list of integers, create a set of the distinct values, and average all distinct elements.
# The second program will take a set quantity of stamps and their countries, and use the add operator to determine how many countries we have stamps from.


### Average Numbers begins here.
def average(array):
    # Instantiate an empty set and the Boolean variable we will use.
    set = []
    equivalence = False
    # Traverse the list and append all unique values to the empty set.
    for number in array:
        for value in set:
            if number != value:
                equivalence = False
            else:
                equivalence = True
                break
        if equivalence is True:
            pass
        else:
            set.append(number)
    # Create variables for the sum of the numbers and the number of elements.
    sum = 0
    length = len(set)
    for number in set:
        sum += number
    final_solution = sum/length
    return final_solution


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)


### Stamp Collector begins here.
# Instantiate a set
s = set()
# Take a fixed quantity as input and initialize variables.
stamp_quantity = int(input())
equivalence = False
# For each new stamp, check if we have already counted the country or not yet. If not, add it to the set.
for _ in range(stamp_quantity):
    country = input()
    for value in s:
        if country != value:
            equivalence = False
        else:
            equivalence = True
            break
    if equivalence is True:
        pass
    else:
        s.add(country)
# Return how many unique countries we have stamps from.
print(len(s))
