import numpy as np

def charpoly(A):
	# A and B are square matrices of order n
	def trace(A, B):
		n, s = len(A), 0
		for i in range(n):
			for j in range(n):
				s += A[i][j] * B[j][i]
		return s
		
	n = len(A)
	m = int(n**0.5)
	pows, poly = {0 : np.eye(n)}, np.zeros(n + 1)
	
	for i in range(1, m + 1):
		pows[i] = np.matmul(pows[i - 1], A)
	
	traces = {i : np.trace(pows[i]) for i in range(m + 1)}
	poly[n], B, k = 1, np.eye(n), 1
	while k < n:
		m = min(m, n - k)
		poly[n - k] = -trace(A, B) / k
		for j in range(1, m):
			poly[n - k - j] = trace(pows[j + 1], B)
			for i in range(j):
				poly[n - k - j] += traces[j - i] * poly[n - k - i]
			poly[n - k - j] /= -(k + j)
		B = np.matmul(pows[m], B)
		for j in range(m):
			B += poly[n - k - j] * pows[m - j - 1]
		k += m
	poly[0] = -trace(A, B) / n
	return poly


# A = np.array([[2, 0], [1, 3]])
# B = np.array([[0, 2, -2], [2, -5, -2], [-2, -2, 0]])
# C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# D = np.array([[1, 2], [3, 4]])
# print(charpoly(A), charpoly(B), charpoly(C), charpoly(D))

	
	
