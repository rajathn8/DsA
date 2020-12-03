# Uses python3
import sys

def gcd_naive(n, m):
    d = 1
    while(d!=0):
        x = n%m
        if x!=0:
            n = m
            m = x
            #print(n,m)
        if x==0:
            d = 0
            #print(m,"Finish")
            return m
 

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))

