def next_fib(a, b):
	return (a + b)

def solve(n):
	a = 1
	b = 2
	sum = 2
	temp = 0
	while temp <= n:
		temp = next_fib(a, b)
		if temp < n:
			a = b
			b = temp
			if not b & 1:
				sum += b
	return sum

for _ in range(int(input())):
	print(solve(int(input())))
