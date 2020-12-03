# Uses python3
import sys

def raj_binary_search(x,y,n):
    low = 0
    high = len(x) - 1
    found = 1
    
    t = -1
    
    if y<x[0] and x[-1]<y:
        found = 0
        
    while low<=high and found==1:
        
        mid = (low+high)//2

        mid_value = x[mid]
            
        if mid_value ==y:
            t = mid
            found = 0

        else:
            if x[low]<= y and y<=x[high]:

                if y< mid_value :
                    high = mid -1
                else: # x[mid]>y
                    low = mid +1
            else:
                found =0

    return t


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    #print(n,'n')
    #print(m,'m')
    #print(a,'a')

    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(raj_binary_search(a, x,n), end = ' ')
