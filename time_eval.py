from numpy.polynomial import Polynomial, polynomial
import numpy as np

class LinearRecurrence:
	def __init__(self, equation, initial_values):
		self.equation = equation # a polynomial describing the equation Fn = a0 F0 + ... + an-1 Fn-1
		self.initialValues = initial_values # a vector of initial values [F0, ..., Fn-1]
		self.order = len(initial_values)
		self.generatingFunction = self.GeneratingFunction(equation, initial_values)
	
	class GeneratingFunction:
		def __init__(self, equation, initial_values):
			tmp = list(reversed(equation))
			self.Q = tmp
			self.P = polynomial.polymul(tmp, initial_values)[:len(equation) - 1:]
	
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
	def oneTerm(self, N):
		return self.oneCoeff(self.generatingFunction.P, self.generatingFunction.Q, N)
		
Fibonacci = LinearRecurrence([-1, -1, 1], [0, 1])
print(Fibonacci.generatingFunction.P, ",", Fibonacci.generatingFunction.Q)
print(Fibonacci.oneTerm(int(input())))






