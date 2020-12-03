# Uses python3
import sys

def get_change(n):
    
    x = n//10
    n = n%10
    
    x = x + n//5
    n = n%5
    
    x = x + n
    
    return x

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
