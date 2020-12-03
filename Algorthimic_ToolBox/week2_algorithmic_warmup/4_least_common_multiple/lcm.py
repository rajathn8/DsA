# Uses python3
import sys

def gcd_supreme(x, y):

    while(y):
        x, y = y, x % y
    return x

def lcm_naive(a, b):
    return int(a*b/gcd_supreme(a,b))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

