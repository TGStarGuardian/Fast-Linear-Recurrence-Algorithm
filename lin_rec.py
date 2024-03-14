from numpy.polynomial import Polynomial, polynomial
import numpy as np

class LinearRecurrence:
	def __init__(self, equation):
		self.equation = equation # a polynomial describing the equation Fn = a0 F0 + ... + an-1 Fn-1
		self.order = len(equation) - 1
		self.generatingFunction = self.GeneratingFunction(equation)
		
	class GeneratingFunction:
		def __init__(self, equation):
			self.Q = np.array(list(reversed(equation)))
		def P(self, initialValues):
			return polynomial.polymul(self.Q, initialValues)[:len(self.Q) - 1:]
			
	def oneCoeff(self, P, Q, N):
		while N:
			T = Q.copy()
			for i in range(1, len(Q), 2):
				T[i] *= -1
			U = polynomial.polymul(P, T)
			if N & 1:
				P = np.array([U[2*i + 1] for i in range(self.order)])
			else:
				P = np.array([U[2*i] for i in range(self.order)])
			A = polynomial.polymul(Q, T)
			Q = np.array([A[2*i] for i in range(self.order + 1)])
			N >>= 1
		return P[0]/Q[0]
	def oneTerm(self, initialValues, N):
		return self.oneCoeff(self.generatingFunction.P(initialValues), self.generatingFunction.Q, N)
	
	# code that computes the power series expansion of 1/Q from x^(N - order + 1) up to x^(N) 
	def sliceCoeff(self, Q, N):
		if not N:
			R = np.array([0 for _ in range(self.order)])
			R[-1] = 1/Q[0]
			return R
		T = Q.copy()
		for i in range(1, len(Q), 2):
			T[i] *= -1
		A = polynomial.polymul(Q, T)
		V = np.array([A[2*i] for i in range(self.order + 1)])
		W = self.sliceCoeff(V, N >> 1)
		S = np.array([0 for _ in range(((len(W) - 1) << 1) + 1)])
		for i in range(len(W)):
			S[i << 1] = W[i]
		if not (N & 1):
			S = polynomial.polymulx(S)
		B = polynomial.polymul(T, S)
		return np.array([B[self.order + i] for i in range(self.order)])
	
	# code that computes the N-th term using the previous function
	def oneCoeffT(self, initialValues, N):
		U = self.sliceCoeff(self.generatingFunction.Q, N)
		return sum(map(lambda x, y : x * y, self.generatingFunction.P(initialValues), reversed(U)))
	
	# code that computes the N-th term of k sequences that satisfy the same equation
	# but may have different initial values
	def vectorNTerm(self, initialValueMatrix, N):
		Q = self.generatingFunction.Q
		P = [self.generatingFunction.P(initialValues) for initialValues in initialValueMatrix]
		U = np.array(list(reversed(self.sliceCoeff(self.generatingFunction.Q, N))))
		R = np.array([0 for _ in range(len(P))])
		for i in range(len(initialValueMatrix)):
			R[i] = sum(map(lambda x, y : x * y, P[i], U))
		return R
		
		
Fibonacci = LinearRecurrence([-1, -1, 1])
print(Fibonacci.oneTerm([0, 1], int(input())))
print(Fibonacci.oneCoeffT([0, 1], int(input())))
print(Fibonacci.vectorNTerm([[0, 1], [0, 1], [1, 1], [2, 2]], 5))




