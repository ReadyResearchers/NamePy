# Author: Jessica Strait
# This project is based on the Sock Merchant challenge on HackerRank. The program must identify the number of pairs of socks available.
# I solved the challenge by using standard dictionary methods.

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    # Instantiate a pair count variable and an empty dictionary.
    pair_count = 0
    new_dictionary = {}
    # Traverse the list given and determine if the element is already in the dictionary. If it is, we can add one to the key.
    # If not, create a new element and assign it key=1: there is at least one sock of that type.
    for index in range(len(ar)):
        element = ar[index]
        if element in new_dictionary:
            new_dictionary[element] += 1
        else:
            new_dictionary[element] = 1
    # Use the numerical keys in the dictionary to determine how many pairs can be made. Pairs can be made until one or zero socks remain.
    for key in new_dictionary:
        element_count = new_dictionary[key]
        while element_count != 1 and element_count != 0:
            pair_count += 1
            element_count -= 2
            # Break statement occurs when no more pairs can be made, and the loop moves to the next key.
            if element_count == 1 or element_count == 0:
                break
    # Return the pair count variable.
    return pair_count


# Code below was included in the HackerRank challenge.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()