# Uses python3
from sys import stdin

def calculateSquareSum_proxy(n): 
    fibo = [0] * (n + 1) 
    if (n <= 0): 
        return 0 
    fibo[0] = 0 
    fibo[1] = 1 
      
    # Initialize result 
    sum = ((fibo[0] * fibo[0]) + 
           (fibo[1] * fibo[1])) 
      
    # Add remaining terms 
    for i in range(2, n + 1): 
        fibo[i] = (fibo[i - 1] + 
                   fibo[i - 2]) 
        sum += (fibo[i] * fibo[i]) 

    return sum%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(calculateSquareSum_proxy(n))
