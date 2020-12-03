# Uses python3
import sys

def fib(n): 
    f = [0] * 1000
    n = int(n) 
  
    # Base cases 
    if (n == 0): 
        return 0
    if (n == 1 or n == 2): 
        return (1)  
  
    # If fib(n) is already computed 
    if (f[n] == True): 
        return f[n]  
  
    k = (n+1)/2 if (n & 1) else n/2
  
    # Applying above formula [Note value n&1  
    # is 1 if n is odd, else 0]. 
    f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) if (n & 1) else (2 * fib(k-1) + fib(k)) * fib(k) 
    return f[n]  
  
# Computes value of first Fibonacci numbers 
def calculateSum(n): 
  
    return fib(n+2) - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(calculateSum(n)%10)
