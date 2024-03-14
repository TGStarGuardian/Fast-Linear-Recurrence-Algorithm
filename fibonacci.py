def fibonacci(N):
	if N < 2:
		return N == 1
	c = 3
	if N & 1:
		a, b = 1, -1
	else:
		a, b = 0, 1
	N >>= 1
	while N > 1:
		if N & 1:
			a = b + a*c
		else:
			b = a + b*c
		c = c*c - 2
		N >>= 1
	return b + a*c

def fibonacci_power_of_2(N):
	if N < 2:
		return N == 1
	b, c = 1, 3
	N >>= 1
	while N > 2:
		b = b*c
		c = c*c - 2
		N >>= 1
	return b*c

print(fibonacci(17), fibonacci_power_of_2(16))
