# Uses python3

# calculate the sum of fibonacci numbers


def fib(n):

	if n <= 1:
		return n

	previousFib = 0
	currentFib = 1

	for i in range(n-1):
		newFib = previousFib + currentFib
		previousFib = currentFib
		currentFib = newFib

	return currentFib


n = int(input())
print(fib(n))
