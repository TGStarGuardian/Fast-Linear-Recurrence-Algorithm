# Fast-Linear-Recurrence-Algorithm
Python implementations of algorithms from https://inria.hal.science/hal-02917827/document. In theory, algorithms presented in the paper offer better time complexities for solving some problems regarding linear recurrence equations.
This repository contains the following algorithms:
* the least significant bit (LSB) algorithm to compute the N-th term of any linear recurrence sequence in time $(2M(d) + d)log(N) + M(d)$, where $M(d)$ is the time needed to multiply two polynomials of degree $d$
* the most significant bit (MSB) algorithm to compute the N-th term of any linear recurrence sequence in time $(3M(d)log(N)$
* an algorithm to compute the power series expansion of $\frac{1}{Q}$ from $N - d + 1$ up to $d - 1$, where $x^d$ is the largest term in $Q(x)$
* an algorithm to compute the N-th term of more than one linear recurrence sequence satisfying the same equation, but differing in initial values. This program runs in time $O(M(d)log(N) + kd)$, where $k$ is the number of sequences
* an algorithm to compute the N-th term of the Fibonacci sequence with initial values 0 and 1 when N is a power of 2
* an algorithm to compute the N-th term of the Fibonacci sequence with initial values 0 and 1 when N is any number
