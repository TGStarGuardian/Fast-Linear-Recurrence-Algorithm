# faster polynomial evaluation
# poly - polynomial
# x - the argument that supports addition, multiplication and scalar multiplication
# e - a function that returns the multiplicative neutral
# zero - a function that returns the additive neutral
# add - addition function
# mul - multiplication function
# scalar_mul - scalar multiplication

def poly_eval(poly, x, e, zero, add, mul, scalar_mul):
	n = len(poly) - 1
	if n < 4:
		return basic_poly_eval(poly, x, e, zero, add, mul, scalar_mul)
	t = int(n**0.5)
	k = t if t * t == n else t + 1
	
	# compute powers up to x^k
	pows = {0 : e()}
	for i in range(1, k + 1):
		pows[i] = mul(pows[i], x)
	
	value = zero()
	
	# Horner's rule when poly is expressed in the form: b0(x) + b1(x) x**k + ... + b_t(x) x**(tk)
	for i in reversed(range(n + 1)):
		m = i % k
		value = add(value, scalar_mul(poly[i], pows[m]))
		if not m and i:
			value = mul(pows[k], value)
	return value
	
def basic_poly_eval(poly, x, e, zero, add, mul, scalar_mul):
	value = zero()
	for i in reversed(range(len(poly))):
		value = mul(x, value)
		value = add(value, scalar_mul(poly[i], e()))
	return value

# import numpy as np
# A = np.array([[2, 0], [1, 3]])
# charpoly = np.array([6, -5, 1])
# print(poly_eval(charpoly, A, lambda : np.eye(len(A)), lambda : np.zeros((len(A), len(A))), lambda x, y : x + y, lambda x, y : np.matmul(x, y), lambda x, y : x * y))






















