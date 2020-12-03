#Uses python3

import sys

from itertools import permutations 

def largest_number_implementation(l): 
    lst = [] 
    for i in permutations(l, len(l)): 
        # provides all permutations of the list values, 
        # store them in list to find max 
        lst.append("".join(map(str,i)))
    return max(lst) 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number_implementation(a))
    
