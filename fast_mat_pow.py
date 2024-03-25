# computes A^N
# A - matrix
# N - power
from charpoly import charpoly
from lin_rec import LinearRecurrence
from poly_eval import poly_eval
import numpy as np

def fast_mat_pow(A, N):
	P = charpoly(A)
	R = LinearRecurrence(P).newModExp(N)
	add = lambda x, y : x + y
	scalar_mul = lambda x, y : x * y
	mul = lambda x, y : np.matmul(x, y)
	zero = lambda : np.zeros(A.shape, dtype = np.longdouble)
	e = lambda : np.eye(len(A), dtype = np.longdouble)
	return poly_eval(R, A, e, zero, add, mul, scalar_mul)

A, N = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], dtype = np.longdouble), 5
print(fast_mat_pow(A, N))
