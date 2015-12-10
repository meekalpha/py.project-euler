def solve(n):
	a = (n - 1)//3 		# number of multiples of 3
	s1 = a*(a + 1)/2 * 3	# sum of these
	b = (n - 1)//5 		# no. multiples of 5
	s2 = b*(b + 1)/2 * 5	# sum of these
	c = (n - 1)//15)  # no. multiples of 15
	s3 = c*(c + 1)/2 * 15 	# sum of these
	sum = s1 + s2 - s3	# inclusion / exclusion

for _ in range(int(input())):
	print(solve(int(input())))
