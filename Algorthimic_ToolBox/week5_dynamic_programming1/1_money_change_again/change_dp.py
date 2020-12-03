# Uses python3
import sys
import math
from math import inf

def change_simple(m):
    # write your code here
    coins = [1, 3, 4]

    min_coin = [None] * (m + 1)

    min_coin[0] = 0

    for i in range(1, m + 1):
        min_coin[i] = inf
        for whole_coin in coins:
            if i >= whole_coin:
                tmp = min_coin[i - whole_coin] + 1
                if tmp < min_coin[i]:
                    min_coin[i] = tmp
            else:
                break

    return min_coin[m]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(change_simple(m))
