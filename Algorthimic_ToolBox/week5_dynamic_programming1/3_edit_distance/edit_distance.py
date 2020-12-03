# Uses python3

import numpy as np
import sys

def distance_edit(s, t):
    
    temp = np.zeros(shape=(len(s) + 1, len(t) + 1), dtype=int)

    for i in range(len(s)+1):
        temp[i, 0] = i
    
    for i in range(len(t)+1):
        temp[0, i] = i

    for i in range(1, len(s) + 1):
        
        for j in range(1, len(t) + 1):
            
            if s[i - 1] == t[j - 1]:
                temp[i, j] = temp[i - 1, j - 1]
            
            else:
                temp[i, j] = 1 + min(temp[i - 1, j], temp[i - 1, j - 1], temp[i, j - 1])

    return (temp[len(s), len(t)])

if __name__ == "__main__":
    print(distance_edit(input(), input()))
