# Uses python3
import sys
#from Levenshtein import *

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions


def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])

    return res


def smart_inverse(a,b):
    
    first = "".join(map(str, a))
    second = "".join(map(str, sorted(first)))
    
    return (LD(first,second))


def merge(a, b, left, ave, right):
    inv_count = 0
    i, j, k = left, ave, left
    while i <= ave - 1 and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            inv_count += ave - i
        k += 1
    while i <= ave - 1:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        a[i] = b[i]
    return inv_count


def merge_sort(a, b, left, right):
    inv_count = 0
    
    if right > left:
        ave = (left + right) // 2
        inv_count += merge_sort(a, b, left, ave)
        inv_count += merge_sort(a, b, ave + 1, right)

        inv_count += merge(a, b, left, ave + 1, right)

    return inv_count


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    #print(get_number_of_inversions(a, b, 0, len(a)))
    #print(smart_inverse(a,b))

    print(merge_sort(a, b, 0, len(a) - 1))
