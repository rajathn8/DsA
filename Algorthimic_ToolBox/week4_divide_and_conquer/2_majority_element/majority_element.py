# Uses python3
import sys

from collections import Counter

def get_majority_element(a, left, right):
    
    d = Counter(a).most_common()[0][1]
    
    if d/len(a)>0.5:
        x = 1
    else:
        x = -1
    return x

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
